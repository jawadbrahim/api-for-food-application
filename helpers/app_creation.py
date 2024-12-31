from flask import Flask
from project.config.development import Development
from flask_swagger_ui import get_swaggerui_blueprint
def create_app(db):
    app = Flask(__name__)
    
    app.config.from_object(Development)
    print(f"Static folder path: {app.static_folder}")
    print(f"Static URL path: {app.static_url_path}")
    db.init_app(app)
    
    with app.app_context():
        from project.features.food_category.route import foods_bp
        from project.features.user.route import user_bp
        from project.features.authentication.routes import auth_bp
        from project.features.chat.route import chat_bp
        from project.features.review.route import review_bp
        app.register_blueprint(foods_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(chat_bp)
        app.register_blueprint(review_bp)
    
        # print(app.url_map)
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Food API"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    
    return app