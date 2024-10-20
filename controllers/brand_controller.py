from models.brand import Brand
from extensions import db
from models.manufacturer import Manufacturer

def get_all_brands():
    return Brand.query.all()

def get_brand_by_id(brand_id):
    return Brand.query.get(brand_id)

def add_brand(name, logo, description, manufacturer_ids):
    brand = Brand(name=name, logo=logo, description=description)
    db.session.add(brand)
    db.session.commit()

    if manufacturer_ids:
        manufacturers = Manufacturer.query.filter(Manufacturer.id.in_(manufacturer_ids)).all()
        brand.manufacturers.extend(manufacturers)
        db.session.commit()

    return brand

def update_brand(brand_id, name, logo, description, manufacturer_ids):
    brand = Brand.query.get(brand_id)
    if not brand:
        return None

    brand.name = name
    brand.logo = logo
    brand.description = description

    if manufacturer_ids is not None:
        brand.manufacturers.clear()
        manufacturers = Manufacturer.query.filter(Manufacturer.id.in_(manufacturer_ids)).all()
        brand.manufacturers.extend(manufacturers)

    db.session.commit()
    return brand


