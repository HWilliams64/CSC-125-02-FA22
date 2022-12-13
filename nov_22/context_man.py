import random

with open('./context_man.py') as file:
    file.read()
    


# enter method
# our code
# exit method
    # file.close()


class MyContext:

    def __init__(self, arg_1, arg_2):
        print("Initializing MyContext", arg_1, arg_2)
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def __enter__(self):
        print("Entering MyContext", self.arg_1, self.arg_2)
        return self

    def __exit__(self, exc_type, exc_value, trace):
        print("Exited MyContext", self.arg_1, self.arg_2)
        print(exc_type, exc_value, trace)
        print('-'*80)

        if issubclass(exc_type, FileExistsError):
            print('This is a FileExistsError')
            return False

        if issubclass(exc_type, ConnectionAbortedError):
            print('This is a ConnectionAbortedError')
            return True

        if issubclass(exc_type, SyntaxError):
            print('This is a SyntaxError')
            return True

with MyContext(1, 2) as my_context:
    print(f"This is my context = {my_context} {my_context.arg_1} {my_context.arg_2}")

    exc = random.choice((Exception, FileExistsError, ConnectionAbortedError, SyntaxError))
    raise exc("This is my random exception")
