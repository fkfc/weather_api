from flask import Flask
from views.weather_api import weather_api
from views.status_api import status_api

app = Flask(__name__)

app.register_blueprint(weather_api)
app.register_blueprint(status_api, url_prefix='/status')
