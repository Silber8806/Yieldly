from app import db

class Planting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seed_id = db.Column(db.Integer, db.ForeignKey('seed.id'))
    seed_grams = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    blackout_date = db.Column(db.Date)
    harvest_date = db.Column(db.Date)
    harvest_grams = db.Column(db.Integer)
    tray_length = db.Column(db.Integer)
    tray_width = db.Column(db.Integer)
    medium = db.Column(db.Text)
    
    def __repr__(self):
        return '<User {}>'.format(self.id)  

class Seed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor = db.Column(db.Text)
    seed_type = db.Column(db.Text)
    batch = db.Column(db.Integer)
    price = db.Column(db.Numeric) 
    seeds = db.relationship('Planting', backref='seed', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.id)  