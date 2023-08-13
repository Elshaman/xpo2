from flask import Flask
from my_blueprint import my_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from products import products

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin@localhost:3310/flask-shopy"
app.register_blueprint(my_blueprint)
app.register_blueprint(products)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Producto




@app.route('/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
