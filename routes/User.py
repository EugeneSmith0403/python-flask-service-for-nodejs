from flask import request
from flask_restful import Resource
from models.User import User as UserModel
from config  import db


class UserRoutes(Resource):
    def get(self):
        res = UserModel.query.all()
        return {
            "UsersList": [i.serialize for i in res]
        }

    def post(self):
        json_data = request.get_json()
        dictionary = dict(json_data)
        dictionary.setdefault('metaData', '')
        dictionary.setdefault('lastName', '')
        dictionary.setdefault('name', '')

        user = UserModel(
            email=dictionary['email'],
            name=dictionary['name'],
            lastName=dictionary['lastName'],
            metaData=dictionary['metaData'],
        )
        db.session.add(user)
        db.session.commit()
        db.session.close()
        return {
            "result": 'Ok'
        }

    def put(self):
        json_data = request.get_json()
        user = UserModel.query.filter(UserModel.email == json_data['email'])
        dictionary = dict(json_data)
        dictionary.pop('_id')
        user.update(dictionary)
        db.session.commit()
        db.session.close()
        return {
            "result": 'Ok'
        }

    def delete(self):
        json_data = request.get_json()
        user = UserModel.query.filter_by(id=json_data['id']).one()
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        return {
            "result": 'Ok'
        }
