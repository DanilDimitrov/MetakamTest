from flask import Blueprint, redirect, render_template, url_for
from controllers.brand_controller import add_brand, get_all_brands
from controllers.manufacturer_controller import add_manufacturer, get_all_manufacturers
from forms.brand_form import BrandForm
from forms.manufacturer_form import ManufacturerForm

admin_client = Blueprint('admin_client', __name__)

@admin_client.route('/client/brands', methods=['GET', 'POST'])
def client_brands():
    form = BrandForm()
    if form.validate_on_submit():
        add_brand(form.name.data, form.logo.data, form.description.data)
        return redirect(url_for('admin_client.client_brands'))
    brands = get_all_brands()
    print(brands)
    return render_template('brands.html', brands=brands, form=form)

@admin_client.route('/client/manufacturers', methods=['GET', 'POST'])
def client_manufacturers():
    form = ManufacturerForm()
    if form.validate_on_submit():
        add_manufacturer(form.name.data, form.description.data, form.country.data, form.certificates.data)
        return redirect(url_for('admin_client.client_manufacturers'))

    manufacturers = get_all_manufacturers()
    return render_template('manufacturers.html', manufacturers=manufacturers, form=form)

