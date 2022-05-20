from datetime import datetime
from flask_restful import Resource, reqparse, abort
from models.votes import Vote
from flask_jwt_extended import jwt_required
from app import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help="firstname обязательное поле")
parser.add_argument('datestart', type=str, required=True, help="lastname обязательное поле")
parser.add_argument('datefinish', type=str, required=True, help="phone обязательное поле")
parser.add_argument('status', type=bool, required=True, help="status обязательное поле")


class VoteResource(Resource):

    def get(self, vote_id):
        return Vote.serialize(
            Vote.query.filter_by(id=vote_id).first_or_404(
                description='Vote не найден'
            )
        )

    def put(self, vote_id):
        vote = Vote.query.filter_by(id=vote_id).first_or_404(
            description='Vote не найден'
        )
        args = parser.parse_args()

        vote.title = args['title']
        vote.datestart = datetime.strptime(args['datestart'], "%Y-%m-%d")
        vote.datefinish = datetime.strptime(args['datefinish'], "%Y-%m-%d")
        vote.status = args['status']
        db.session.commit()

        return {'msg': 'OK', 'data': vote.serialize()}, 200

    def delete(self, vote_id):
        Vote.query.filter_by(id=vote_id).first_or_404(
            description='vote не найден'
        )

        Vote.query.filter_by(id=vote_id).delete()
        db.session.commit()
        return {'msg': 'vote удален'}, 200


class VoteListResource(Resource):

    def post(self):
        args = parser.parse_args()
        vote = Vote(title=args['title'], datestart=datetime.strptime(args['datestart'], "%Y-%m-%d"), datefinish=datetime.strptime(args['datefinish'], "%Y-%m-%d"), status=args['status'])
        db.session.add(vote)
        db.session.commit()
        return {'msg': 'OK', 'data': vote.serialize()}, 201

    def get(self):
        votes = Vote.query.all()
        return [Vote.serialize(item) for item in votes]