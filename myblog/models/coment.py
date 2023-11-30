from datetime import datetime
from myblog import db

class Coment(db.Model):
    __tablename__ = 'coments'
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, author, body) -> None:
        self.author = author
        self.body = body

    def __repr__(self) -> str:
        return f'Coment: {self.author}'