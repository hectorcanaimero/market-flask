from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine


app = Flask(__name__)
db = MongoEngine()
db.init_app(app)
app.config.from_object('config')
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from app.resources import shop, category, products, order, customer