import random

class MyClass():
    var_1 = 'a'
    var_2 = 2
    var_3 = True

    def __init__(self, arg_1=None, arg_2=None, arg_3=None):
        self.var_1 = arg_1 or self.var_1
        self.var_2 = arg_2 or self.var_2
        self.var_3 = arg_3 or self.var_3

        if self.var_3 > 4:
            self.var_4 = random.randint(4, 10)

        if self.var_2 < 4:
            self.var_4 = random.randint(12, 100)

    def combine(self, other_instance:'MyClass'):
        new_class = MyClass()
        new_class.var_1 = self.var_1 + other_instance.var_1
        new_class.var_2 = self.var_2 + other_instance.var_2
        new_class.var_3 = self.var_3 + other_instance.var_3
        new_class.var_4 = self.var_4 + other_instance.var_4

        return new_class

    def get_var_1(self):
        return self.var_1

    def set_var_1(self, value):
        self.var_1 = value

    def __str__(self) -> str:
        return f"v1: {self.var_1} v2: {self.var_2} v3: {self.var_3} v4: {self.var_4}"

instances = []
for _ in range(10):
    instances.append(MyClass(1, 2, 3))

instance_1 = MyClass(1, 2, 3)
instance_2 = MyClass(4, 5, 6)
print(' sec 1 '.center(40, '='))
print('instance 1:', instance_1)
print('instance 2:', instance_2)

# instance_1.var_1 = 'Taco'
# instance_1.var_2 = 3.14
# instance_1.var_3 = False

# print(' sec 2 '.center(40, '='))
# print('instance 1:', instance_1.get_var_1())
# print('instance 2:', instance_2.get_var_1())

# print(' sec 3 '.center(40, '='))
# instance_1.set_var_1(random.randint(1, 10))
# instance_2.set_var_1(random.randint(1, 10))

# print('instance 1:', instance_1.get_var_1())
# print('instance 2:', instance_2.get_var_1())

# print(' sec 4 '.center(40, '='))
# print('instance 1:', instance_1)
# print('instance 2:', instance_2)

print(' sec 5 '.center(40, '='))

instance_3 = instance_1.combine(instance_2)

for i in instances:
    instance_3 = instance_3.combine(i)

print('instance 3:', instance_3)
