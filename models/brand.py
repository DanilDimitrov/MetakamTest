from extensions import db

brand_manufacturer = db.Table('brand_manufacturer',
    db.Column('brand_id', db.Integer, db.ForeignKey('brand.id'), primary_key=True),
    db.Column('manufacturer_id', db.Integer, db.ForeignKey('manufacturer.id'), primary_key=True)
)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    logo = db.Column(db.String(200))
    description = db.Column(db.Text)
    manufacturers = db.relationship('Manufacturer', secondary=brand_manufacturer, lazy='subquery',
                                    backref=db.backref('brands', lazy=True))
