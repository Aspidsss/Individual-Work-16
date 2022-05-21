from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.comment import Comment
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('blog_id', type=int, required=True, help="blog_id обязательное поле")
parser.add_argument('author_id', type=int, required=True, help="author_id обязательное поле")
parser.add_argument('content', type=str, required=True, help="content обязательное поле")
parser.add_argument('date_comment', type=str, required=True, help="date_comment обязательное поле")


class CommentResource(Resource):
    @jwt_required()
    def get(self, comment_id):
        return Comment.serialize(
            Comment.query.filter_by(id=comment_id).first_or_404(
                description='Comment не найден'
            )
        )

    @jwt_required()
    def put(self, comment_id):
        comment = Comment.query.filter_by(id=comment_id).first_or_404(
            description='Comment не найден'
        )
        args = parser.parse_args()

        comment.blog_id = args['blog_id']
        comment.author_id = args['author_id']
        comment.content = args['content']
        comment.date_comment = datetime.strptime(args['date_comment'], "%Y-%m-%d")
        db.session.commit()

        return {'msg': 'OK', 'data': comment.serialize()}, 200

    @jwt_required()
    def delete(self, comment_id):
        Comment.query.filter_by(id=comment_id).first_or_404(
            description='Comment не найден'
        )

        Comment.query.filter_by(id=comment_id).delete()
        db.session.commit()
        return {'msg': 'Comment удален'}, 200


class CommentListResource(Resource):
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        comment = Comment(blog_id=args['blog_id'], author_id = args['author_id'], content = args['content'], date_comment = datetime.strptime(args['date_comment'], "%Y-%m-%d"))
        db.session.add(comment)
        db.session.commit()
        return {'msg': 'OK', 'data': comment.serialize()}, 201

    @jwt_required()
    def get(self):
        comments = Comment.query.all()
        return [Comment.serialize(item) for item in comments]