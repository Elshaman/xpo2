from flask import Blueprint

my_blueprint = Blueprint('my_blueprint' , __name__)

@my_blueprint.route('/')
def index():
    return "dentro del blueprint"