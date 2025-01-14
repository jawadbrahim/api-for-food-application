from flask import Flask
from project.config.development import Development
from project.features.firebase.firebase_init import init_credential

def create_app(db):
    app = Flask(__name__)
    
    app.config.from_object(Development)
    init_credential()
    # print(f"static_folder: {app.static_folder}")
    db.init_app(app)
    
    
    
    with app.app_context():
        from project.features.food_category.route import foods_bp
        from project.features.user.route import user_bp
        from project.features.authentication.routes import auth_bp
        from project.features.chat.route import chat_bp
        from project.features.review.route import review_bp
        from project.features.firebase.routes import firebase_bp
        
        app.register_blueprint(foods_bp)
        app.register_blueprint(user_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(chat_bp)
        app.register_blueprint(review_bp)
        app.register_blueprint(firebase_bp)
        
        
        
        # print(app.url_map)
    
    return app
