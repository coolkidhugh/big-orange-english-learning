from flask import Blueprint, request, jsonify
from user import db
from src.models.word import Word, UserWord, QuizResult
import random
import jwt
import os

quiz_bp = Blueprint('quiz', __name__)

# 验证令牌的装饰器函数
def token_required(f):
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({'message': '缺少认证令牌'}), 401
        
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(
                token, 
                os.environ.get('SECRET_KEY', 'asdf#FGSgvasgf$5$WGT'),
                algorithms=['HS256']
            )
            user_id = payload['sub']
        except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return jsonify({'message': '无效或过期的令牌'}), 401
        
        return f(user_id, *args, **kwargs)
    
    decorated.__name__ = f.__name__
    return decorated

# 获取测验题目
@quiz_bp.route('/generate', methods=['GET'])
@token_required
def generate_quiz(user_id):
    quiz_type = request.args.get('type', 'image_to_english')
    count = request.args.get('count', 10, type=int)
    use_user_words = request.args.get('use_user_words', 'false') == 'true'
    
    # 获取单词池
    if use_user_words:
        words = UserWord.query.filter_by(user_id=user_id).all()
        if len(words) < count:
            # 如果用户单词不足，补充预设单词
            preset_words = Word.query.filter_by(is_preset=True).limit(count - len(words)).all()
            words.extend(preset_words)
    else:
        words = Word.query.filter_by(is_preset=True).all()
    
    # 随机选择单词
    if len(words) < count:
        count = len(words)
    
    selected_words = random.sample(words, count)
    
    # 根据测验类型准备题目
    questions = []
    for word in selected_words:
        if quiz_type == 'image_to_english':
            questions.append({
                'id': word.id,
                'question_type': 'image_to_english',
                'image_path': word.image_path,
                'answer': word.english
            })
        else:  # chinese_to_english
            questions.append({
                'id': word.id,
                'question_type': 'chinese_to_english',
                'chinese': word.chinese,
                'answer': word.english
            })
    
    return jsonify({
        'quiz_type': quiz_type,
        'questions': questions,
        'total_questions': len(questions)
    }), 200

# 提交测验结果
@quiz_bp.route('/submit', methods=['POST'])
@token_required
def submit_quiz(user_id):
    data = request.get_json()
    
    if not data or 'quiz_type' not in data or 'score' not in data or 'total_questions' not in data:
        return jsonify({'message': '缺少必要信息'}), 400
    
    # 创建测验结果记录
    quiz_result = QuizResult(
        user_id=user_id,
        quiz_type=data['quiz_type'],
        score=data['score'],
        total_questions=data['total_questions']
    )
    
    db.session.add(quiz_result)
    db.session.commit()
    
    return jsonify({
        'message': '测验结果已保存',
        'result': {
            'id': quiz_result.id,
            'quiz_type': quiz_result.quiz_type,
            'score': quiz_result.score,
            'total_questions': quiz_result.total_questions,
            'created_at': quiz_result.created_at
        }
    }), 201

# 获取用户测验历史
@quiz_bp.route('/history', methods=['GET'])
@token_required
def get_quiz_history(user_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    results = QuizResult.query.filter_by(user_id=user_id).order_by(
        QuizResult.created_at.desc()
    ).paginate(page=page, per_page=per_page, error_out=False)
    
    return jsonify({
        'results': [{
            'id': result.id,
            'quiz_type': result.quiz_type,
            'score': result.score,
            'total_questions': result.total_questions,
            'percentage': (result.score / result.total_questions) * 100 if result.total_questions > 0 else 0,
            'created_at': result.created_at
        } for result in results.items],
        'total': results.total,
        'pages': results.pages,
        'current_page': page
    }), 200
