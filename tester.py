import random
import sorting

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

l = generate_list(100, 10)

sorting.insertion_sort(l)

print(l)