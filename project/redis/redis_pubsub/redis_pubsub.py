import redis
import json
import threading
redis_client = redis.Redis(host='localhost', port=6379, db=0)
def notify_typing(room_id, user_id):
    message = {'room_id': room_id, 'user_id': user_id, 'event': 'typing'}
    redis_client.publish('chat_typing', json.dumps(message))
    print(f"Published typing event for user {user_id} in room {room_id}.")
def listen_for_typing_events():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('chat_typing')
    for message in pubsub.listen():
        if message['type'] == 'message':
            typing_event = json.loads(message['data'])
            handle_typing_event(typing_event)
def handle_typing_event(typing_event):
    print(f"User {typing_event['user_id']} is typing in room {typing_event['room_id']}.")


def start_typing_event_listener():
    listener_thread = threading.Thread(target=listen_for_typing_events)
    listener_thread.daemon = True
    listener_thread.start()
