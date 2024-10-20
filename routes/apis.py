from flask import Blueprint, jsonify, request
from controllers.brand_controller import get_all_brands, get_brand_by_id, add_brand, update_brand
from controllers.manufacturer_controller import get_all_manufacturers, get_manufacturer_by_id, add_manufacturer

apis = Blueprint('apis', __name__)

@apis.route('/api/v1/brands', methods=['GET', 'POST'])
def api_get_brands():
    if request.method == 'POST':
        data = request.get_json()
        brand = add_brand(data['name'], data.get('logo'), data.get('description'), data.get('manufacturers', []))
        return jsonify({
            'id': brand.id,
            'name': brand.name,
            'logo': brand.logo,
            'description': brand.description,
            'manufacturers': [{'id': manufacturer.id, 'name': manufacturer.name} for manufacturer in brand.manufacturers]
        }), 201

    brands = get_all_brands()
    return jsonify([
        {
            'id': brand.id,
            'name': brand.name,
            'logo': brand.logo,
            'description': brand.description,
            'manufacturers': [{'id': manufacturer.id, 'name': manufacturer.name} for manufacturer in brand.manufacturers]
        } for brand in brands
    ])

@apis.route('/api/v1/brands/<int:id>', methods=['GET', 'PUT'])
def api_get_brand(id):
    if request.method == 'PUT':
        data = request.get_json()
        brand = update_brand(id, data['name'], data.get('logo'), data.get('description'), data.get('manufacturers', []))
        return jsonify({
            'id': brand.id,
            'name': brand.name,
            'logo': brand.logo,
            'description': brand.description,
            'manufacturers': [{'id': manufacturer.id, 'name': manufacturer.name} for manufacturer in brand.manufacturers]
        })

    brand = get_brand_by_id(id)
    return jsonify({
        'id': brand.id,
        'name': brand.name,
        'logo': brand.logo,
        'description': brand.description,
        'manufacturers': [{'id': manufacturer.id, 'name': manufacturer.name} for manufacturer in brand.manufacturers]
    })

# Routes for Manufacturers
@apis.route('/api/v1/manufacturers', methods=['GET', 'POST'])
def api_get_manufacturers():
    if request.method == 'POST':
        data = request.get_json()
        manufacturer = add_manufacturer(data['name'], data.get('description', ''), 
                                         data.get('country'), data.get('certificates'))
        return jsonify({
            'id': manufacturer.id,
            'name': manufacturer.name,
            'description': manufacturer.description,
            'country': manufacturer.country,
            'certificates': manufacturer.certificates
        }), 201

    manufacturers = get_all_manufacturers()
    return jsonify([
        {
            'id': manufacturer.id,
            'name': manufacturer.name,
            'description': manufacturer.description,
            'country': manufacturer.country,
            'certificates': manufacturer.certificates
        } for manufacturer in manufacturers
    ])

@apis.route('/api/v1/manufacturers/<int:id>', methods=['GET'])
def api_get_manufacturer(id):
    manufacturer = get_manufacturer_by_id(id)
    return jsonify({
        'id': manufacturer.id,
        'name': manufacturer.name,
        'description': manufacturer.description,
        'country': manufacturer.country,
        'certificates': manufacturer.certificates
    })
