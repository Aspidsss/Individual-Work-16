from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.choice import Choice
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('question_id', type=int, required=True, help="question_id обязательное поле")
parser.add_argument('user_id', type=int, required=True, help="user_id обязательное поле")
parser.add_argument('choice', type=str, required=True, help="choice обязательное поле")


class ChoiceResource(Resource):

    def get(self, choice_id):
        return Choice.serialize(
            Choice.query.filter_by(id=choice_id).first_or_404(
                description='Choice не найден'
            )
        )

    def put(self, choice_id):
        choice = Choice.query.filter_by(id=choice_id).first_or_404(
            description='Choice не найден'
        )
        args = parser.parse_args()

        choice.question_id = args['question_id']
        choice.user_id = args['user_id']
        choice.choice = args['choice']
        db.session.commit()

        return {'msg': 'OK', 'data': choice.serialize()}, 200

    def delete(self, choice_id):
        Choice.query.filter_by(id=choice_id).first_or_404(
            description='Choice не найден'
        )

        Choice.query.filter_by(id=choice_id).delete()
        db.session.commit()
        return {'msg': 'Choice удален'}, 200


class ChoiceListResource(Resource):

    def post(self):
        args = parser.parse_args()
        choice = Choice(user_id=args['user_id'], question_id=args['question_id'], choice=args['choice'])
        db.session.add(choice)
        db.session.commit()
        return {'msg': 'OK', 'data': choice.serialize()}, 201

    def get(self):
        choices = Choice.query.all()
        return [Choice.serialize(item) for item in choices]