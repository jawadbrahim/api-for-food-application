from functools import wraps
from flask import request, jsonify
from pydantic import ValidationError
import inspect

def validate_schema(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                validated_data = schema(**request.json)
            except ValidationError as e:
                return jsonify({"errors": e.errors()}), 400
            
            # Extract token_id from kwargs
            token_id = kwargs.get('token_id')
            
            # Determine if the wrapped function accepts 'token_id'
            func_params = inspect.signature(func).parameters
            if 'token_id' in func_params:
                return func(*args, **kwargs, validated_data=validated_data, token_id=token_id)
            else:
                return func(*args, **kwargs, validated_data=validated_data)
        
        return wrapper
    return decorator

