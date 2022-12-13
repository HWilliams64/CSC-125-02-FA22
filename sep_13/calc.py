import sys
value_1 = input("Please type a number: ")

if not value_1.isdigit():
    print(f"\"{value_1}\" is an invalid number")
    sys.exit(1)

operator = input("Please type \"add\" or \"sub\": ")

if operator != "add" and operator != "sub":
    print(f"\"{operator}\" is an invalid operator. It must be \"add\" or \"sub\"")
    sys.exit(1)


value_3 = input("Please type a number: ")

if not value_3.isnumeric():
    print(f"\"{value_3}\" is an invalid number")
    sys.exit(1)

num_1 = int(value_1)
num_2 = int(value_3)

if operator == "add":
    result = num_1 + num_2
    print(f"{result} = {num_1} + {num_2}")

elif operator == "sub":
    result = num_1 - num_2
    print(f"{result} = {num_1} - {num_2}")
