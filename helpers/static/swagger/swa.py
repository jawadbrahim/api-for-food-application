# swagger_app.py

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_FOOD_URL = '/api/docs/food'
FOOD_API_URL = '/static/swagger.yaml'
swaggerui_blueprint_food = get_swaggerui_blueprint(
        SWAGGER_FOOD_URL, FOOD_API_URL, config={'app_name': "Food API"}
    )
swaggerui_blueprint_food.name = "swagger_ui_food"

app.register_blueprint(swaggerui_blueprint_food, url_prefix=SWAGGER_FOOD_URL)

if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8000)
