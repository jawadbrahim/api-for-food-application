from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError

def validate_schema(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                validated_data = schema(**request.json)
            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 400
            return func(*args, **kwargs, validated_data=validated_data)
        return wrapper
    return decorator
