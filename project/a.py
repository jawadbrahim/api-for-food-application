import redis

# Check if Redis class exists
print(dir(redis))  # Should list all attributes, including 'Redis'

# Initialize Redis client
r = redis.Redis(host='localhost', port=6379, db=0)

# Test Redis connection
r.set('test_key', 'test_value')
print(r.get('test_key').decode('utf-8'))
