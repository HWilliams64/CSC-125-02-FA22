'''for i in range(5):
    print('hello world')'''

def my_function():
    print('hello world')

def for_loop(max_iterations, func, iterations=0):

    if iterations + 1 < max_iterations:
        for_loop(max_iterations, func, iterations+1)
    
    func()


for_loop(5, my_function)
