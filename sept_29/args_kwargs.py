# Positional arguments have to come before keyword arguments

def my_function(*args, x=None, y=None):
    print(f"pos args: {args} x: {x} y: {y}")
    return sum(args)


#r = my_function(1, 2, 3, 4, 5, x="A", y="B")
def addition(x, y=0, z=0):
    return x + y + z

def my_kwargs_function(*args, **kwargs):
    print(f"pos args: {args} keyword args: {kwargs}")

my_kwargs_function()

# DRY => DONT REPEAT YOURSELF