from myblog import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self) -> str:
        return f'User: {self.username}'
