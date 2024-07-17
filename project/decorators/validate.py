from functools import wraps, partial
from flask import abort, request, jsonify, make_response
from pydantic import ValidationError


def validate_input(func=None, *, args_schema=None, json_schema=None):
    if func is None:
        return partial(validate_input, args_schema=args_schema, json_schema=json_schema)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            inputs={}
            if args_schema:
                inputs = args_schema(**request.args)

            if json_schema:
                inputs = json_schema(**request.json)
        except ValidationError as e:
            print(str(e))
            abort(make_response(jsonify(errors=str(e)), 400))
        else:
            return func(*args, **kwargs, inputs=inputs)

    return wrapper