import json
import os
import datetime

with open('./example.json') as file:
    py_obj = json.load(file)  # convert json string to a python object
    #print(py_obj)


py_dict = {
    'key_1': 1,
    'key_2': 2,
    'key_3': str(datetime.datetime.now()),
}

for i in range(100):
    py_dict[f'k-{i}'] = i


with open('./example_w.json', 'w') as file:
    json.dump(py_dict, file)


class MyClass:

    def __init__(self):
        self.var_1 = 1
        self._var_2 = 2
        self._var_3 = 3

    def make_var_4(self):
        self.var_4 = 6


my_class = MyClass()
my_class.make_var_4()
my_class_dict = my_class.__dict__
print(my_class_dict)
    
