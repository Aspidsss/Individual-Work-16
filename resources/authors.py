from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.author import Author
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('first_name', type=str, required=True, help="firstname обязательное поле")
parser.add_argument('last_name', type=str, required=True, help="last_name обязательное поле")
parser.add_argument('email', type=str, required=True, help="email обязательное поле")
parser.add_argument('phone', type=str, required=True, help="phone обязательное поле")
parser.add_argument('date_registration', type=str, required=True, help="date_registration обязательное поле")


class AuthorResource(Resource):
    @jwt_required()
    def get(self, author_id):
        return Author.serialize(
            Author.query.filter_by(id=author_id).first_or_404(
                description='Author не найден'
            )
        )

    @jwt_required()
    def put(self, author_id):
        author = Author.query.filter_by(id=author_id).first_or_404(
            description='Author не найден'
        )
        args = parser.parse_args()

        author.first_name = args['first_name']
        author.last_name = args['last_name']
        author.email = args['email']
        author.phone = args['phone']
        author.date_registration = datetime.strptime(args['date_registration'], "%Y-%m-%d")
        db.session.commit()

        return {'msg': 'OK', 'data': author.serialize()}, 200

    @jwt_required()
    def delete(self, author_id):
        Author.query.filter_by(id=author_id).first_or_404(
            description='Author не найден'
        )

        Author.query.filter_by(id=author_id).delete()
        db.session.commit()
        return {'msg': 'Author удален'}, 200


class AuthorListResource(Resource):
    @jwt_required()
    def post(self):
        args = parser.parse_args()
        author = Author(first_name=args['first_name'], last_name=args['last_name'], email=args['email'], phone=args['phone'], date_registration=datetime.strptime(args['date_registration'], "%Y-%m-%d"))
        db.session.add(author)
        db.session.commit()
        return {'msg': 'OK', 'data': author.serialize()}, 201

    @jwt_required()
    def get(self):
        authors = Author.query.all()
        return [Author.serialize(item) for item in authors]