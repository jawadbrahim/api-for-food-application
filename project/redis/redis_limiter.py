# from limits.storage import RedisStorage
# from limits import RateLimitItemPerMinute
# from limits.strategies import MovingWindowRateLimiter

# def get_rate_limiter(limit=10, per_minute=True):
#     storage = RedisStorage("redis://:jawadibrahim10@localhost:6379")
#     limiter = MovingWindowRateLimiter(storage)
#     rate_limit = RateLimitItemPerMinute(limit) if per_minute else RateLimitItemPerMinute(limit * 60)
#     return limiter, rate_limit