from app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="blogs")
    title = db.Column(db.String(64))
    content = db.Column(db.String(64))
    date = db.Column(db.DateTime)

    comments = db.relationship("Comment", back_populates="blog")

    def serialize(self):
        return {
            'id': self.id,
            'author': self.author.serialize(),
            'title': self.title,
            'content': self.content,
            'date': self.date.isoformat(),
        }
