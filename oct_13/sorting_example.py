

import random

# [1,2,3,4,5]
# [2,4,1,3,5]

my_list = [random.randint(1, 100) for _ in range(10)]

def apple(value):
    if value % 2 == 0:
        # the number is even
        value -= 100
    else:
        # the number is odd
        value += 100
    return value


my_list.sort(key=apple)

print(my_list)
