from flask_restful import Resource, reqparse, abort
from models.users import User
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('firstname', type=str, required=True, help="firstname обязательное поле")
parser.add_argument('lastname', type=str, required=True, help="lastname обязательное поле")
parser.add_argument('phone', type=str, required=True, help="phone обязательное поле")
parser.add_argument('email', type=str, required=True, help="email обязательное поле")
parser.add_argument('status', type=bool, required=True, help="status обязательное поле")
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

        user.firstname = args['firstname']
        user.lastname = args['lastname']
        user.email = args['email']
        user.phone = args['phone']
        user.status = args['status']
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
        user = User(firstname=args['firstname'], lastname=args['lastname'], email=args['email'], phone=args['phone'], status=args['status'])
        user.set_password(args['password'])
        db.session.add(user)
        db.session.commit()
        return {'msg': 'OK', 'data': user.serialize()}, 201

    def get(self):
        users = User.query.all()
        return [User.serialize(item) for item in users]