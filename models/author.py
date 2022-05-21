from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    date_registration = db.Column(db.DateTime)

    comments = db.relationship("Comment", back_populates="author")
    blogs = db.relationship("Blog", back_populates="author")


    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'date_registration': self.date_registration.isoformat(),
        }
