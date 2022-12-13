import time


def long_running_func(length):
    print('Im going to sleep now')
    time.sleep(length)
    print('Im wake')

ms_time_stamp = int(round(time.time() * 1000))
print(ms_time_stamp)
long_running_func(10)
ms_time_stamp = int(round(time.time() * 1000))
print(ms_time_stamp)
