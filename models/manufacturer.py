from extensions import db

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(50))
    certificates = db.Column(db.String(200))
