import redis
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def save_session(session_id, data):

    redis_client.set(session_id, json.dumps(data))


def get_session(session_id):

    data = redis_client.get(session_id)

    if data:
        return json.loads(data)

    return {}