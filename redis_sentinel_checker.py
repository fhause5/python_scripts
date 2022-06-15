from redis.sentinel import Sentinel
import time

time_checker = 5

while True:
    try:
        sentinel = Sentinel([
            ('127.0.0.1', 26379),
            ('127.0.0.1', 26380),
        ])
        master_redis = sentinel.discover_master('mymaster')
        print("[INFO] Connected to Redis, master is: " + str(master_redis)  + "\nChecking every: " + str(time_checker) + " sec")
        time.sleep(time_checker)
    except:
        print('[WARNING] Disconected from redis' + "\nChecking every: " + str(time_checker) + " sec")
        time.sleep(time_checker)
