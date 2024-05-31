"""
Various sorting algorithms.
"""

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

def merge_sort(items):
    """
    Sort items in ascending order using Merge Sort method.
    """
    # a 1-item list is considered a sorted list
    if len(items) == 1:
        return items
    m = len(items) // 2
    a = merge_sort(items[:m])
    b = merge_sort(items[m:])
    result = []
    while (len(a) > 0) or (len(b) > 0):
        # if all a items taken, take from b
        if len(a) == 0:
            result.append(b.pop(0))
        # if b empty take from a, or take the lower of a[0] vs b[0]
        elif (len(b) == 0) or (a[0] < b[0]):
            result.append(a.pop(0))
        # take from b if b[0] >= a[0]
        else:
            result.append(b.pop(0))
    return result
    
def bubble_sort(items):
    """
    Sort items in ascending order using Bubble Sort method.
    """
    for i in range(len(items)):
        # values up to the ith position from end are already sorted
        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                t = items[j]
                items[j] = items[j+1]
                items[j+1] = t

def selection_sort(items):
    """
    Sort items in ascending order using Selection Sort method.
    """
    for i in range(len(items)):
        # track lowest value seen in loop
        low = i
        for j in range(i+1, len(items)):
            if items[j] < items[low]:
                low = j
        # swap lowest value to position i if lower than value at i
        if low != i:
            t = items[i]
            items[i] = items[low]
            items[low] = t

        
          
            
    
