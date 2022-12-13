my_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, "one", "two", "three", "four", "five", "six"]
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, "one", "two", "three", "four", "five", "six")

assert my_list[0] == my_tuple[0]
assert my_list[-2] == my_tuple[-2]


assert my_tuple.count("one") == my_list.count("one")


user_color = input("Please enter your a color:")
acceptable_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'orange')


for v in my_tuple:
    print(v)