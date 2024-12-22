from functools import wraps
from flask import jsonify, request
from project.redis.redis_limiter import get_rate_limiter

limiter, rate_limit = get_rate_limiter(limit=10, per_minute=True)

def rate_limiter_decorator():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_ip = request.remote_addr
            if not limiter.hit(rate_limit, user_ip):
                return jsonify({"error": "Too many requests"}), 429
            
            return func(*args, **kwargs)
        
        return wrapper
    return decorator
