from config import db


class MetaData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(80), unique=False, nullable=False)
    website = db.Column(db.String(120), unique=False, nullable=False)
    facebook = db.Column(db.String(120), unique=False, nullable=False)
    instagram = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<MetaData %r>' % self.project

    @property
    def serialize(self):
       return {
           'id': self.id,
           'project': self.project,
           'website'  : self.website,
           'facebook': self.facebook,
           'instagram': self.instagram
       }
