from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
REQUEST_API = Blueprint('request_api', __name__)

# Defines the Swagger URL, the API to the JSON file of swagger's data, and the blueprint of swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Portal-Shavit-swagger"
    }
)