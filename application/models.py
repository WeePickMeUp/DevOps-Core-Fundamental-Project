from application import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    orders = db.relationship('Groups', backref= 'groups')

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_id = db.Column(db.Integer, db.ForeignKey('name.id'))
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
