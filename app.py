import os
from threading import Thread

from flask import *
from flask_migrate import Migrate
from flask_restful import Api

from config import db
from rabbitMq.index import RabbitMq
from routes.MetaData import MetaDataRoutes
from routes.User import UserRoutes

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

api.add_resource(UserRoutes, '/users')
api.add_resource(MetaDataRoutes, '/metaData')


def createSecondThread():
    RabbitMq().init()


thread = Thread(target=createSecondThread)
thread.start()

if __name__ == "__main__":
    thread.close()
