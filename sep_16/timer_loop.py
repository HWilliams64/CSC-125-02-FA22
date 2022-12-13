import time

expiration = time.time() + 30 # 30 seconds in the future
count = 0 
while expiration > time.time(): # Continue while the current time is less then the future time
    count += 1
    print(f"Count: {count}", end="\r")
    time.sleep(1)

