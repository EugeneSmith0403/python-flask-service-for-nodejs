from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    lastName = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    metaData = db.Column(db.JSON, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastName': self.lastName,
            'email': self.email,
            'metaData': self.metaData
        }
