import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def save_memory(user, message):
    r.lpush(user, message)

def get_memory(user):
    return r.lrange(user, 0, 10)