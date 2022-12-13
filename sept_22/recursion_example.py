# DRY => DONT REPEAT YOURSELF

def for_loop(max_iterations, iterations = 0):
    print(f"{iterations} - {max_iterations}")

    if iterations+1 < max_iterations:
        returned_val = for_loop(max_iterations, iterations+1)
        print(returned_val)

    return (" " * (iterations+1))+ str(iterations)


for_loop(5)
# fib numbers