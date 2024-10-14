import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def notify_typing(room_id, user_id):
    message = {'room_id': room_id, 'user_id': user_id, 'event': 'typing'}
    redis_client.publish('chat_typing', json.dumps(message))
