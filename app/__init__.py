from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


from resources.users import UserResource, UserListResource
from resources.votes import VoteResource, VoteListResource
from resources.questions import QuestionResource, QuestionListResource
from resources.choice import ChoiceResource, ChoiceListResource

api.add_resource(UserListResource, '/api/users', endpoint='users')
api.add_resource(UserResource, '/api/users/<int:user_id>', endpoint='user')
api.add_resource(VoteListResource, '/api/votes', endpoint='votes')
api.add_resource(VoteResource, '/api/votes/<int:vote_id>', endpoint='vote')
api.add_resource(QuestionListResource, '/api/questions', endpoint='questions')
api.add_resource(QuestionResource, '/api/questions/<int:question_id>', endpoint='question')

api.add_resource(ChoiceListResource, '/api/choices', endpoint='choices')
api.add_resource(ChoiceResource, '/api/choices/<int:choice_id>', endpoint='choice')

