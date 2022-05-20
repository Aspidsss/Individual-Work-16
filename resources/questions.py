from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.questions import Question
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('vote_id', type=int, required=True, help="vote_id обязательное поле")
parser.add_argument('content', type=str, required=True, help="content обязательное поле")
parser.add_argument('datevote', type=str, required=True, help="datevote обязательное поле")


class QuestionResource(Resource):

    def get(self, question_id):
        return Question.serialize(
            Question.query.filter_by(id=question_id).first_or_404(
                description='Question не найден'
            )
        )

    def put(self, question_id):
        question = Question.query.filter_by(id=question_id).first_or_404(
            description='Question не найден'
        )
        args = parser.parse_args()

        question.vote_id = args['vote_id']
        question.datevote = datetime.strptime(args['datevote'], "%Y-%m-%d")
        question.content = args['content']
        db.session.commit()

        return {'msg': 'OK', 'data': question.serialize()}, 200

    def delete(self, question_id):
        Question.query.filter_by(id=question_id).first_or_404(
            description='Question не найден'
        )

        Question.query.filter_by(id=question_id).delete()
        db.session.commit()
        return {'msg': 'Question удален'}, 200


class QuestionListResource(Resource):

    def post(self):
        args = parser.parse_args()
        question = Question(vote_id=args['vote_id'], datevote=datetime.strptime(args['datevote'], "%Y-%m-%d"), content=args['content'])
        db.session.add(question)
        db.session.commit()
        return {'msg': 'OK', 'data': question.serialize()}, 201

    def get(self):
        questions = Question.query.all()
        return [Question.serialize(item) for item in questions]