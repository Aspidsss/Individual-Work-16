from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.blog import Blog
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('author_id', type=int, required=True, help="author_id обязательное поле")
parser.add_argument('title', type=str, required=True, help="title обязательное поле")
parser.add_argument('content', type=str, required=True, help="content обязательное поле")
parser.add_argument('date', type=str, required=True, help="date обязательное поле")

class BlogResource(Resource):
    @jwt_required()
    def get(self, blog_id):
        return Blog.serialize(
            Blog.query.filter_by(id=blog_id).first_or_404(
                description='Blog не найден'
            )
        )

    @jwt_required()
    def put(self, blog_id):
        blog = Blog.query.filter_by(id=blog_id).first_or_404(
            description='Blog не найден'
        )
        args = parser.parse_args()

        blog.author_id = args['author_id']
        blog.title = args['title']
        blog.content = args['content']
        blog.date = datetime.strptime(args['date'], "%Y-%m-%d")
        db.session.commit()

        return {'msg': 'OK', 'data': blog.serialize()}, 200

    @jwt_required()
    def delete(self, blog_id):
        Blog.query.filter_by(id=blog_id).first_or_404(
            description='Blog не найден'
        )

        Blog.query.filter_by(id=blog_id).delete()
        db.session.commit()
        return {'msg': 'Blog удален'}, 200


class BlogListResource(Resource):
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        blog = Blog(author_id=args['author_id'], title=args['title'], content=args['content'], date=datetime.strptime(args['date'], "%Y-%m-%d"))
        db.session.add(blog)
        db.session.commit()
        return {'msg': 'OK', 'data': blog.serialize()}, 201

    @jwt_required()
    def get(self):
        blogs = Blog.query.all()
        return [Blog.serialize(item) for item in blogs]