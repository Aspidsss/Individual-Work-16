from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    email = db.Column(db.String(64))
    status = db.Column(db.Boolean)
    password = db.Column(db.String(128))

    choices = db.relationship("Choice", back_populates="user")

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'phone': self.phone,
            'email': self.email,
            'status': self.status
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)