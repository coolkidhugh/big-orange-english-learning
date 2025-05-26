from user import db
from datetime import datetime

class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(100), nullable=False)
    chinese = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    audio_path = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_preset = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Word {self.english}>'

class UserWord(db.Model):
    __tablename__ = 'user_words'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    chinese = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    audio_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<UserWord {self.english}>'

class QuizResult(db.Model):
    __tablename__ = 'quiz_results'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_type = db.Column(db.String(50), nullable=False)  # 'image_to_english' or 'chinese_to_english'
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<QuizResult {self.quiz_type} {self.score}/{self.total_questions}>'
