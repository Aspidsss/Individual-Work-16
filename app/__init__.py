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
    return make_response(jsonify({"error": "Not Found"}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({"error": "Internal Server Error"}), 500)


from resources import auth
from resources.users import UserResource, UserListResource
from resources.authors import AuthorResource, AuthorListResource
from resources.comments import CommentResource, CommentListResource
from resources.blogs import BlogResource, BlogListResource

api.add_resource(UserListResource, "/api/users", endpoint="users")
api.add_resource(UserResource, "/api/users/<int:user_id>", endpoint="user")

api.add_resource(AuthorListResource, "/api/authors", endpoint="authors")
api.add_resource(AuthorResource, "/api/authors/<int:author_id>", endpoint="author")
# {
#     "first_name": "sergey",
#     "last_name": "koksharov",
#     "email": "sergey.email",
#     "phone": "+7 900 000 00 00",
#     "date_registration": "2022-05-19"
# }
api.add_resource(CommentListResource, "/api/comments", endpoint="comments")
api.add_resource(CommentResource, "/api/comments/<int:comment_id>", endpoint="comment")
# {
#     "blog_id":  1,
#     "author_id": 1,
#     "content": "test content for api",
#     "date_comment": "2022-05-19"
# }

api.add_resource(BlogListResource, "/api/blogs", endpoint="blogs")
api.add_resource(BlogResource, "/api/blogs/<int:blog_id>", endpoint="blog")
# {
#     "author_id": 1,
#     "title": "test title for api",
#     "content": "test content for api",
#     "date": "2022-05-19"
# }
api.add_resource(auth.UserLogin, "/api/login")
api.add_resource(auth.UserRegistration, "/api/registration")
api.add_resource(auth.UserLogoutAccess, "/api/logout/access")
api.add_resource(auth.UserLogoutRefresh, "/api/logout/refresh")
api.add_resource(auth.TokenRefresh, "/api/token/refresh")