from flask import Blueprint, request, jsonify
from src.models.user import db, User
import jwt
import datetime
import os
import hashlib

# 创建蓝图
user_bp = Blueprint('user', __name__)

# 密钥
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')

# 用户注册
@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    
    # 检查用户名是否已存在
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"message": "用户名已存在"}), 400
    
    # 检查邮箱是否已存在
    existing_email = User.query.filter_by(email=data['email']).first()
    if existing_email:
        return jsonify({"message": "邮箱已被注册"}), 400
    
    # 密码加密
    password_hash = hashlib.sha256(data['password'].encode()).hexdigest()
    
    # 创建新用户
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=password_hash
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "注册成功"}), 201

# 用户登录
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    
    # 查找用户
    user = User.query.filter_by(username=data['username']).first()
    
    # 验证密码
    if not user or user.password != hashlib.sha256(data['password'].encode()).hexdigest():
        return jsonify({"message": "用户名或密码错误"}), 401
    
    # 生成令牌
    token = jwt.encode({
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, SECRET_KEY, algorithm='HS256')
    
    return jsonify({
        "message": "登录成功",
        "token": token,
        "user_id": user.id,
        "username": user.username
    }), 200

# 获取用户信息
@user_bp.route('/profile', methods=['GET'])
def profile():
    # 获取令牌
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({"message": "未提供有效的认证令牌"}), 401
    
    token = auth_header.split(' ')[1]
    
    try:
        # 验证令牌
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
        
        # 查找用户
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "用户不存在"}), 404
        
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at
        }), 200
    
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "令牌已过期"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "无效的令牌"}), 401

# 验证令牌的装饰器
def token_required(f):
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"message": "未提供有效的认证令牌"}), 401
        
        token = auth_header.split(' ')[1]
        
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            user = User.query.get(user_id)
            if not user:
                return jsonify({"message": "用户不存在"}), 404
            
            return f(user, *args, **kwargs)
        
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "令牌已过期"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "无效的令牌"}), 401
    
    return decorated
