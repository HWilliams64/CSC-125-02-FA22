import random
import traceback

# Service level agreement  SLA 
# 99%
# 99.9%. DDOS => Distributed denial of service attack 

try:
    v = random.randint(0, 1)
    print(v)
    if v:
        raise ValueError("This is my random error")

    print("There are no issue with the code")

except ValueError as e:
    #traceback.print_exc()
    print(f"I have handled the error. Reason: {e}")