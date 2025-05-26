from flask import Blueprint, request, jsonify
from src.models.word import Word, UserWord
import os
import uuid
import datetime

# 创建蓝图
word_bp = Blueprint('word', __name__)

# 获取预设单词
@word_bp.route('/preset', methods=['GET'])
def get_preset_words():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 12, type=int)
    category = request.args.get('category', '')
    
    query = Word.query.filter_by(is_preset=True)
    
    if category:
        query = query.filter_by(category=category)
    
    pagination = query.paginate(page=page, per_page=per_page)
    
    words = []
    for word in pagination.items:
        words.append({
            'id': word.id,
            'english': word.english,
            'chinese': word.chinese,
            'image_path': word.image_path,
            'audio_path': word.audio_path,
            'category': word.category
        })
    
    return jsonify({
        'words': words,
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200

# 获取用户上传的单词
@word_bp.route('/user', methods=['GET'])
def get_user_words():
    from src.routes.user import token_required
    
    @token_required
    def get_words(current_user):
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 12, type=int)
        
        pagination = UserWord.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=per_page)
        
        words = []
        for user_word in pagination.items:
            word = user_word.word
            words.append({
                'id': word.id,
                'english': word.english,
                'chinese': word.chinese,
                'image_path': word.image_path,
                'audio_path': word.audio_path,
                'category': word.category,
                'created_at': user_word.created_at
            })
        
        return jsonify({
            'words': words,
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page
        }), 200
    
    return get_words()

# 上传单词
@word_bp.route('/upload', methods=['POST'])
def upload_word():
    from src.routes.user import token_required
    
    @token_required
    def upload(current_user):
        english = request.form.get('english')
        chinese = request.form.get('chinese')
        
        # 检查必填字段
        if not english or not chinese:
            return jsonify({"message": "英文单词和中文翻译为必填项"}), 400
        
        # 检查图片
        if 'image' not in request.files:
            return jsonify({"message": "请上传图片"}), 400
        
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({"message": "未选择图片文件"}), 400
        
        # 保存图片
        image_filename = f"{uuid.uuid4()}{os.path.splitext(image_file.filename)[1]}"
        image_path = f"/static/uploads/{image_filename}"
        image_file.save(os.path.join('src/static/uploads', image_filename))
        
        # 处理音频（可选）
        audio_path = None
        if 'audio' in request.files and request.files['audio'].filename != '':
            audio_file = request.files['audio']
            audio_filename = f"{uuid.uuid4()}{os.path.splitext(audio_file.filename)[1]}"
            audio_path = f"/static/uploads/{audio_filename}"
            audio_file.save(os.path.join('src/static/uploads', audio_filename))
        
        # 创建单词
        word = Word(
            english=english,
            chinese=chinese,
            image_path=image_path,
            audio_path=audio_path,
            is_preset=False
        )
        
        # 保存到数据库
        from src.models.user import db
        db.session.add(word)
        db.session.flush()
        
        # 创建用户单词关联
        user_word = UserWord(
            user_id=current_user.id,
            word_id=word.id
        )
        
        db.session.add(user_word)
        db.session.commit()
        
        return jsonify({
            "message": "单词上传成功",
            "word": {
                "id": word.id,
                "english": word.english,
                "chinese": word.chinese,
                "image_path": word.image_path,
                "audio_path": word.audio_path
            }
        }), 201
    
    return upload()

# 删除用户单词
@word_bp.route('/user/<int:word_id>', methods=['DELETE'])
def delete_user_word(word_id):
    from src.routes.user import token_required
    
    @token_required
    def delete(current_user, word_id):
        from src.models.user import db
        
        user_word = UserWord.query.filter_by(user_id=current_user.id, word_id=word_id).first()
        
        if not user_word:
            return jsonify({"message": "单词不存在或不属于当前用户"}), 404
        
        db.session.delete(user_word)
        db.session.commit()
        
        return jsonify({"message": "单词删除成功"}), 200
    
    return delete(word_id)
