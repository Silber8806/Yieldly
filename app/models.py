from app import db

class Planting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.Integer, db.ForeignKey('seed.id'))

    def __repr__(self):
        return '<User {}>'.format(self.id)  

class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seeds = db.relationship('Planting', backref='seed', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.id)  