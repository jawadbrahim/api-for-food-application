from flask import Flask
from project.config.development import Development

def create_app(db):
    app = Flask(__name__)
    
    app.config.from_object(Development)
    
    db.init_app(app)
    
    with app.app_context():
        from project.features.food_category.route import foods_bp
        from project.features.user.route import user_bp
        from project.features.authentication.routes import auth_bp
        from project.features.chat.route import chat_bp
        app.register_blueprint(foods_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(chat_bp)
    
        print(app.url_map)
    
    return app