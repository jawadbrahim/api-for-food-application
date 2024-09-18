from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError
import inspect

def validate_schema(json_schema=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if json_schema:
                    validated_data = json_schema(**request.json)
                else:
                    return jsonify({"error": "No schema provided"}), 400
            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 400
            
            token_id = kwargs.get('token_id')
            func_params = inspect.signature(func).parameters
            if 'token_id' in func_params:
                return func(*args, **kwargs, validated_data=validated_data, token_id=token_id)
            else:
                return func(*args, **kwargs, validated_data=validated_data)
        
        return wrapper
    return decorator
