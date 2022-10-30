from . import db

class Position (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    department = db.Column(db.String(30))
    wage = db.Column(db.Integer)

    def __repr__(self):
        return self.name


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    birth_date = db.Column(db.Date)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    position = db.relationship('Position', backref=db.backref('employee', lazy='dynamic'))


    def __repr__(self):
        return self.name
