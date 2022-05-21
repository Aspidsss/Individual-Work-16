from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    login = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def serialize(self):
        return {
            'id': self.id,
            'login': self.login,
            'password': self.password
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)