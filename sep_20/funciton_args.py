# f(x) => x + 1
# f(2) => 2 + 1

def banana(x, y):
    if x > y: 
        return x + y
    elif x < y:
        return x - y
    else:
        return x ** y
# X^Y
for x in range(3):
    for y in range(3):
        print(f"x:{x} y:{y}")
        result = banana(x, y)
        print(result)