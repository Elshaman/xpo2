from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, DataRequired,NumberRange

class ProductFormMixin():
    nombre = StringField('nombre del producto',
                          validators=[InputRequired(message="nombre es requerido")])
    precio = IntegerField('precio del producto',
                          validators=[InputRequired(message="precio es requerido"),
                                      NumberRange(min=10, max=1000000, message='bla')])

class NewProductForm(FlaskForm , ProductFormMixin):
    imagen = FileField("Imagen del producto",  validators=[FileRequired(message="archivo requerido"), FileAllowed(['jpg', 'png'], 'images only!')])
    submit = SubmitField('Add')

class EditProductForm(FlaskForm, ProductFormMixin):
    submit = SubmitField('Edit')

