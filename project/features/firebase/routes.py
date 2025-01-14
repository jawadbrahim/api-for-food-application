from .blueprints import firebase_bp
from .firebase_user import get_user_by_id,list_all_users,create_user
from flask import jsonify
from .request_validator import request_validator
@firebase_bp.route("/user/<user_id>",methods=["GET"])
def get_users(user_id):
    user=get_user_by_id(user_id)
    if user:
        return jsonify(user)
@firebase_bp.route("/firebase_users",methods=["GET"])
def get_list_users():
    users=list_all_users()
    return jsonify(users)
@firebase_bp.route("/create_user",methods=["POST"])
@request_validator.valdiate_create_user()
def create_users(validated_data):
    users=create_user(validated_data)
    return jsonify(users)