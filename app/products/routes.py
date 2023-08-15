from flask import render_template, flash, redirect
from . import products
from .forms import NewProductForm, EditProductForm
import app

@products.route('/')
def index():
    p = app.models.Producto.query.all()
    return render_template('list.html', productos = p)

@products.route('/create', methods =[ 'GET' , 'POST'])
def create():
    p = app.models.Producto()
    form_registro = NewProductForm()
    if form_registro.validate_on_submit():
        form_registro.populate_obj(p)
        ##p = app.models.Producto(nombre = form_registro.nombre.data , precio= form_registro.precio.data)
        app.db.session.add(p)
        app.db.session.commit()
        flash( "registro exitoso")
        return redirect('/products')
    return render_template('new.html', form=form_registro)

@products.route('/edit/<product_id>' , methods =[ 'GET' , 'POST'])
def edit(product_id):
    p = app.models.Producto.query.get(product_id)
    form_edit = EditProductForm(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        return "actualizacion exitosa"
    return render_template("new.html" , form = form_edit)


