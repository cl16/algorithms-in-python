import random
import sorting

def funcAndResult(f):
    """
    Decorator to show which function is called whenever results are tested.
    Prints original args object for in-place results, and return value for
    non-in-place results.
    """
    def wrapper(*args):
        print(f'FUNCTION: {f.__name__}')
        print('Args before:'.ljust(12), *args)
        result = f(*args)
        print('Args after:'.ljust(12), *args)
        print('Return: '.ljust(12), result)
        return result
    return wrapper

def generate_list(m, n):
    """
    Generate list of n random numbers from range 0-m.

    param m: int
    param n: int
    returns: list
    """
    result = []
    for i in range(n):
        result.append(random.randint(0, m))
    return result

# generate a test list
l = generate_list(100, 10)

# use decorator and call wrapper function on data
# decorator shows function called and result
funcAndResult(sorting.merge_sort)(l)

