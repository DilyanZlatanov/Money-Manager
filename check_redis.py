import redis

def check_redis_connection(host='localhost', port=6379, db=0):
    try:
        client = redis.StrictRedis(host=host, port=port, db=db)
        response = client.ping()
        if response:
            print("✅ Redis работи! PONG получен.")
        else:
            print("⚠️ Redis отговори, но не както се очаква.")
    except redis.ConnectionError as e:
        print(f"❌ Грешка при връзка с Redis: {e}")
    except Exception as e:
        print(f"❌ Друга грешка: {e}")

if __name__ == "__main__":
    check_redis_connection()
