from app import db


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64))
    datestart = db.Column(db.DateTime)
    datefinish = db.Column(db.DateTime)
    status = db.Column(db.Boolean)

    questions = db.relationship("Question", back_populates="vote")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'datestart': self.datestart.isoformat(),
            'datefinish': self.datefinish.isoformat(),
            'status': self.status
        }
