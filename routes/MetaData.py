from flask import request
from flask_restful import Resource

from models.MetaData import MetaData as MetaDataModel
from config  import db


class MetaDataRoutes(Resource):
    def get(self):
        res = MetaDataModel.query.all()
        return {
            "metaDataList": [i.serialize for i in res]
        }

    def post(self):
        json_data = request.get_json()
        dictionary = dict(json_data)

        data = MetaDataModel(
            project=dictionary.get('project', ''),
            website=dictionary.get('website', ''),
            facebook=dictionary.get('facebook', ''),
            instagram=dictionary.get('instagram', '')
        )
        db.session.add(data)
        db.session.commit()
        return {
            "result": 'Ok'
        }

    def put(self):
        json_data = request.get_json()
        data = MetaDataModel.query.filter(MetaDataModel.id == json_data['id'])
        data.update(dict(json_data))
        db.session.commit()
        return {
            "result": 'Ok'
        }

    def delete(self):
        json_data = request.get_json()
        data = MetaDataModel.query.filter_by(id=json_data['id']).one()
        db.session.delete(data)
        db.session.commit()
        return {
            "result": 'Ok'
        }
