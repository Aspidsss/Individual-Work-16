from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    blog = db.relationship("Blog", back_populates="comments")

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author", back_populates="comments")

    content = db.Column(db.String(64))
    date_comment = db.Column(db.DateTime)


    def serialize(self):
        return {
            'id': self.id,
            'blog':  self.blog.serialize(),
            'author': self.author.serialize(),
            'content': self.content,
            'date_comment': self.date_comment.isoformat(),
        }
