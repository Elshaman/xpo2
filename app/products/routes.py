from flask import render_template
from . import products
from .forms import RegisterProductForm
import app

@products.route('/')
def index():
    p = app.models.Producto.query.all()
    return render_template('list.html', productos = p)

@products.route('/create', methods =[ 'GET' , 'POST'])
def create():
    form_registro = RegisterProductForm()
    if form_registro.validate_on_submit():
        p = app.models.Producto(nombre = form_registro.nombre.data , precio= form_registro.precio.data)
        app.db.session.add(p)
        app.db.session.commit()
        return "registro exitoso"
    return render_template('new.html', form=form_registro)

@products.route('/edit/<int:product_id>')
def edit(product_id):



