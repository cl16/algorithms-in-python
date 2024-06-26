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

def test(a, m=100, n=10):
    """
    Run a simple test on algorithm a, using a randomly-generated
    test list of integers.

    param a: function, sorting algorithm
    param m: random number maximum, i.e. range 0-m
    param n: length of test list
    return: None
    """
    l = generate_list(m, n)
    funcAndResult(a)(l)

if __name__ == '__main__':
    # generate test list 
    l = generate_list(100, 10)
    
    # print out algorithm, test data, result
    funcAndResult(sorting.merge_sort)(l)

