from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,  SubmitField

class RegisterProductForm(FlaskForm):
    nombre = StringField('nombre del producto' )
    precio = StringField('precio del producto' )
    submit = SubmitField('Registrar producto')