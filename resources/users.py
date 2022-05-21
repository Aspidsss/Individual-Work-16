from flask_restful import Resource, reqparse, abort
from models.users import User
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('login', type=str, required=True, help="login обязательное поле")
parser.add_argument('password', type=str, required=True, help="password обязательное поле")


class UserResource(Resource):

    def get(self, user_id):
        return User.serialize(
            User.query.filter_by(id=user_id).first_or_404(
                description='Пользователь не найден'
            )
        )

    def put(self, user_id):
        user = User.query.filter_by(id=user_id).first_or_404(
            description='Пользователь не найден'
        )
        args = parser.parse_args()

        user.login = args['login']
        db.session.commit()

        return {'msg': 'OK', 'data': user.serialize()}, 200

    def delete(self, user_id):
        User.query.filter_by(id=user_id).first_or_404(
            description='Пользователь не найден'
        )

        User.query.filter_by(id=user_id).delete()
        db.session.commit()
        return {'msg': 'Пользователь удален'}, 200


class UserListResource(Resource):

    def post(self):
        args = parser.parse_args()
        user = User(login=args['login'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()
        return {'msg': 'OK', 'data': user.serialize()}, 201

    def get(self):
        users = User.query.all()
        return [User.serialize(item) for item in users]