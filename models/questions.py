from app import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote_id = db.Column(db.Integer, db.ForeignKey('vote.id'))
    vote = db.relationship("Vote", back_populates="questions")
    content = db.Column(db.String(64))
    datevote = db.Column(db.DateTime)

    choices = db.relationship("Choice", back_populates="question")

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'datevote': self.datevote.isoformat(),
            'vote': self.vote.serialize()
        }
