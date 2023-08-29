from flask import Blueprint

products = Blueprint('productos', __name__, url_prefix='/products' ,
                     template_folder='templates',
                     static_folder= 'images')

from . import routes