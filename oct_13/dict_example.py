# key : value,
my_list = [1, 2, 3, 4, 5]
my_dict = {"one": 1, "two": 2, "three": 3, "ten":67}

# add
my_dict['four'] = 4
my_dict.update({"five": 5, "six": 6})  # set.update() list.append()

# replace
for i in range(5):
    my_dict[f'={i}='] = i

value = my_list[4]
print(value)

value = my_dict["ten"]
value = my_dict.get("ten", 'unknown')
value = my_dict.setdefault("ten", 10)
print(value)

print(my_dict)
