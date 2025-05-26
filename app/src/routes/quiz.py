from flask import Blueprint, request, jsonify
from src.models.word import Word, UserWord, QuizResult
import random

# 创建蓝图
quiz_bp = Blueprint('quiz', __name__)

# 生成测验题目
@quiz_bp.route('/generate', methods=['GET'])
def generate_quiz():
    from src.routes.user import token_required
    
    @token_required
    def generate(current_user):
        quiz_type = request.args.get('type', 'image_to_english')
        count = request.args.get('count', 10, type=int)
        use_user_words = request.args.get('use_user_words', 'false').lower() == 'true'
        
        # 获取预设单词
        preset_words = Word.query.filter_by(is_preset=True).all()
        
        # 获取用户单词
        user_words = []
        if use_user_words:
            user_word_relations = UserWord.query.filter_by(user_id=current_user.id).all()
            for relation in user_word_relations:
                user_words.append(relation.word)
        
        # 合并单词列表
        all_words = preset_words + user_words
        
        # 如果单词数量不足，减少测验题目数量
        if len(all_words) < count:
            count = len(all_words)
        
        # 随机选择单词
        selected_words = random.sample(all_words, count)
        
        questions = []
        for word in selected_words:
            question = {
                'id': word.id,
                'question_type': quiz_type,
                'answer': word.english
            }
            
            if quiz_type == 'image_to_english':
                question['image_path'] = word.image_path
            else:  # chinese_to_english
                question['chinese'] = word.chinese
            
            questions.append(question)
        
        return jsonify({
            'questions': questions,
            'count': len(questions)
        }), 200
    
    return generate()

# 提交测验结果
@quiz_bp.route('/submit', methods=['POST'])
def submit_quiz():
    from src.routes.user import token_required
    
    @token_required
    def submit(current_user):
        data = request.json
        
        quiz_type = data.get('quiz_type')
        score = data.get('score')
        total_questions = data.get('total_questions')
        
        if not quiz_type or score is None or total_questions is None:
            return jsonify({"message": "缺少必要参数"}), 400
        
        # 计算百分比
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0
        
        # 创建测验结果
        quiz_result = QuizResult(
            user_id=current_user.id,
            quiz_type=quiz_type,
            score=score,
            total_questions=total_questions,
            percentage=percentage
        )
        
        # 保存到数据库
        from src.models.user import db
        db.session.add(quiz_result)
        db.session.commit()
        
        return jsonify({
            "message": "测验结果已保存",
            "result": {
                "id": quiz_result.id,
                "quiz_type": quiz_result.quiz_type,
                "score": quiz_result.score,
                "total_questions": quiz_result.total_questions,
                "percentage": quiz_result.percentage,
                "created_at": quiz_result.created_at
            }
        }), 201
    
    return submit()

# 获取测验历史
@quiz_bp.route('/history', methods=['GET'])
def get_quiz_history():
    from src.routes.user import token_required
    
    @token_required
    def get_history(current_user):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        pagination = QuizResult.query.filter_by(user_id=current_user.id).order_by(
            QuizResult.created_at.desc()
        ).paginate(page=page, per_page=per_page)
        
        results = []
        for result in pagination.items:
            results.append({
                'id': result.id,
                'quiz_type': result.quiz_type,
                'score': result.score,
                'total_questions': result.total_questions,
                'percentage': result.percentage,
                'created_at': result.created_at
            })
        
        return jsonify({
            'results': results,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }), 200
    
    return get_history()
