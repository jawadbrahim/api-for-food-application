import redis
import json
import threading

# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Notify function to publish typing events
def notify_typing(room_id, user_id):
    message = {'room_id': room_id, 'user_id': user_id, 'event': 'typing'}
    redis_client.publish('chat_typing', json.dumps(message))
    print(f"Published typing event for user {user_id} in room {room_id}.")

# Subscribe and listen for typing events
def listen_for_typing_events():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('chat_typing')

    # Listen for new messages
    for message in pubsub.listen():
        if message['type'] == 'message':
            typing_event = json.loads(message['data'])
            handle_typing_event(typing_event)

# Handle typing event when received
def handle_typing_event(typing_event):
    print(f"User {typing_event['user_id']} is typing in room {typing_event['room_id']}.")

# Run the listener in a separate thread to simulate event-based behavior
def start_typing_event_listener():
    listener_thread = threading.Thread(target=listen_for_typing_events)
    listener_thread.daemon = True  # This will allow the thread to exit when the main program exits
    listener_thread.start()
