def fun_raise_error():
    raise KeyboardInterrupt('This is my error')
    x = 1 + 1
    return x

def fun_d():
    x = fun_raise_error()
    print(x)

def fun_c():
    try:
        fun_d()
    except FileExistsError:
        print('Function C has saved the day')

def fun_b():
    try:
        fun_c()
    except (ValueError, ConnectionError):
        print('Function B has saved the day')
    except KeyboardInterrupt:
        print('Function B has saved the day 2')

def fun_a():
    try:
        fun_b()
    except TypeError:
        print('Function A has saved the day')


try:
    fun_a()
except Exception as e:
    message = str(e)
    print(f'Global has saved the day. The error said: "{e}"')
