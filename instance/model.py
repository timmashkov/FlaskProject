from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Класс(таблица) для нашей базы данных, в ней прописан
    дандер метод для строкового представления"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return f'User: {self.id}, {self.username}, {self.email}, {self.created_at}'


class User(db.Model):
    """Класс(таблица) для нашей базы данных, в ней прописан
    дандер метод для строкового представления"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text(300), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return f'User: {self.id}, {self.username}, {self.email}, {self.created_at}'
