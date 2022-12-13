# List comprehension
# my_list = [ value_add for value_add in values logical_expression ]

'''my_list = []
for i in range(10):
    if i >= 5:
        my_list.append(i)

my_list = [i for i in range(10) if i >= 5]
print(my_list)

my_dict = {f"{chr(i)}":i for i in range(200,250)}
print(my_dict)
'''
abc = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {letter: i+1 for i, letter in enumerate(abc)}
print(my_dict)
