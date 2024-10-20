from models.manufacturer import Manufacturer
from extensions import db

def get_all_manufacturers():
    return Manufacturer.query.all()

def get_manufacturer_by_id(manufacturer_id):
    return Manufacturer.query.get(manufacturer_id)

def add_manufacturer(name, description, country, certificates):
    new_manufacturer = Manufacturer(name=name, description=description, country=country, certificates=certificates)
    db.session.add(new_manufacturer)
    db.session.commit()
    return new_manufacturer
