from app import db


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship("Question", back_populates="choices")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="choices")
    choice = db.Column(db.String(32))

    def serialize(self):
        return {
            'id': self.id,
            'question': self.question.serialize(),
            'user': self.user.serialize(),
            'choice': self.choice
        }
