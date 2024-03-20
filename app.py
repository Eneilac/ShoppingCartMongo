from flask import Flask
from blueprints.products import blueprint as products_blueprint

app = Flask(__name__)
app.register_blueprint(products_blueprint)
# TODO: Add the other blueprints here