
def insertion_sort(items):
    """
    Sort items in-place in ascending order using Insertion Sort method.
    """
    i = 1
    while i < len(items):
        j = i - 1
        while (j >= 0) and (items[i] < items[j]):
                j -= 1
        t = items[i]
        s = i - 1
        while s > j:
             items[s + 1] = items[s]
             s -= 1
        items[s + 1] = t
        i += 1
    #return items
