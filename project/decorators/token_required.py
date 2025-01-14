from functools import wraps
from flask import request, jsonify
from project.model.token import Token 
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401
        token_record = Token.query.filter_by(token=token, is_deleted=False).first()
        if not token_record:
            return jsonify({"message": "Invalid Token!"}), 401
        kwargs['token_id'] = token_record.id
        return f(*args, **kwargs)
    return decorated_function

