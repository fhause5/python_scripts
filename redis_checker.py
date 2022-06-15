import redis
import time

redis_host = '127.0.0.1'
redis_password = '1234'
time_checker = 5

r = redis.Redis(host=redis_host, socket_connect_timeout=1, password=redis_password)  # short timeout for the test

while True:
    try:
        r.ping()
        print('[INFO] Connected to redis "{}"'.format(redis_host) + "\nCheck every: " + str(time_checker) + " sec")
        time.sleep(time_checker)
    except:
        print('[WARNING] Disconected from redis "{}"'.format(redis_host) + "\nCheck every: " + str(time_checker) + " sec")
        time.sleep(time_checker)
