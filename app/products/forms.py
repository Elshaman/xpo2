from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField, FileField

class ProductFormMixin():
    nombre = StringField('nombre del producto' )
    precio = StringField('precio del producto' )

class NewProductForm(FlaskForm , ProductFormMixin):
    imagen = FileField("Imagen del producto")
    submit = SubmitField('Add')

class EditProductForm(FlaskForm, ProductFormMixin):
    submit = SubmitField('Edit')

