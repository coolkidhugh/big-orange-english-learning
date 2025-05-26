import csv
import os
import random
from user import db
from models.word import Word
from flask import Flask

# 创建一个临时的Flask应用上下文
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:password@localhost:3306/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 预设单词类别
categories = ['animals', 'food', 'daily', 'nature', 'transport']

# 示例单词数据（英文-中文-类别）
sample_words = [
    # 动物类
    ('cat', '猫', 'animals'),
    ('dog', '狗', 'animals'),
    ('elephant', '大象', 'animals'),
    ('tiger', '老虎', 'animals'),
    ('lion', '狮子', 'animals'),
    ('rabbit', '兔子', 'animals'),
    ('bird', '鸟', 'animals'),
    ('fish', '鱼', 'animals'),
    ('monkey', '猴子', 'animals'),
    ('bear', '熊', 'animals'),
    
    # 食物类
    ('apple', '苹果', 'food'),
    ('banana', '香蕉', 'food'),
    ('bread', '面包', 'food'),
    ('cake', '蛋糕', 'food'),
    ('rice', '米饭', 'food'),
    ('noodle', '面条', 'food'),
    ('egg', '鸡蛋', 'food'),
    ('meat', '肉', 'food'),
    ('vegetable', '蔬菜', 'food'),
    ('fruit', '水果', 'food'),
    
    # 日常用品类
    ('chair', '椅子', 'daily'),
    ('table', '桌子', 'daily'),
    ('bed', '床', 'daily'),
    ('lamp', '灯', 'daily'),
    ('phone', '电话', 'daily'),
    ('computer', '电脑', 'daily'),
    ('book', '书', 'daily'),
    ('pen', '笔', 'daily'),
    ('bag', '包', 'daily'),
    ('clock', '时钟', 'daily'),
    
    # 自然类
    ('sun', '太阳', 'nature'),
    ('moon', '月亮', 'nature'),
    ('star', '星星', 'nature'),
    ('sky', '天空', 'nature'),
    ('cloud', '云', 'nature'),
    ('rain', '雨', 'nature'),
    ('snow', '雪', 'nature'),
    ('mountain', '山', 'nature'),
    ('river', '河', 'nature'),
    ('sea', '海', 'nature'),
    
    # 交通类
    ('car', '汽车', 'transport'),
    ('bus', '公交车', 'transport'),
    ('train', '火车', 'transport'),
    ('airplane', '飞机', 'transport'),
    ('bicycle', '自行车', 'transport'),
    ('ship', '船', 'transport'),
    ('motorcycle', '摩托车', 'transport'),
    ('taxi', '出租车', 'transport'),
    ('subway', '地铁', 'transport'),
    ('helicopter', '直升机', 'transport'),
]

def generate_sample_data():
    with app.app_context():
        # 创建数据库表
        db.create_all()
        
        # 检查是否已有预设单词
        existing_count = Word.query.filter_by(is_preset=True).count()
        if existing_count > 0:
            print(f"已存在 {existing_count} 个预设单词，跳过导入")
            return
        
        print("开始导入预设单词...")
        
        # 导入示例单词
        for english, chinese, category in sample_words:
            # 为每个单词生成一个图片路径（实际项目中应该有真实图片）
            image_path = f"images/{category}/{english}.jpg"
            
            # 创建单词记录
            word = Word(
                english=english,
                chinese=chinese,
                image_path=image_path,
                category=category,
                is_preset=True
            )
            
            db.session.add(word)
        
        # 提交到数据库
        db.session.commit()
        print(f"成功导入 {len(sample_words)} 个预设单词")

if __name__ == "__main__":
    generate_sample_data()
