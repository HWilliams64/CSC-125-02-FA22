# is -  checks the identity of variables, means they in the same location
# in memory

# == - checks if the value in the memory location is the same

var_1 = "happy panda" * 1000
var_2 = "happy panda" * 1000

print(id(var_1))
print(id(var_2))
print(f'Equals: {var_1 == var_2}')
print(f'Identical: {var_1 is var_2}')


x = 1
x = 2
print(8)
