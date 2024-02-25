from flask import Flask
from flask_cors import CORS
from api.views import views

app = Flask(__name__)
CORS(app)

app.register_blueprint(views, url_prefix="/api")
