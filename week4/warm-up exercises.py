def find_maximum ( lst ):
    """ Returns the maximum value in the list . """
    max_val = lst [0]
    for x in lst :
        if x > max_val :
            max_val = x
    return max_val
"""
this is a linear O(n) as it iterates through only one list 
then returns the max value
"""

def is_sorted ( lst ):
    """ Returns True if the list is sorted """
    for i in range (1 , len ( lst )):
        if lst [i] < lst [i - 1]:
            return False
    return True
"""
this costs n to do as it only iterates through one list
"""

def sum_all_pairs ( lst ):
    """ Returns a list of sums for each pair in list ."""
    result = []
    n = len ( lst )
    for i in range (n):
        for j in range (i + 1 , n):
            result.append(lst[i] + lst[j])
    return result
"""
this costs n^2 to do as for every iteration of the first for 
loop there is another for loop iterating.
"""

def counter (n):
    """ Halves n until it becomes less than or equal to 1."""
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps
"""
the function is logarithmic as it only iterates through parts of n
"""

def my_function ( lst ):
    total = 0
    for i in lst :
        x = len(lst)
        while x > 1:
            total += 1
            x //= 2
    return total
"""
the function is logarithmic in nature as it does not iterate for every value for every inwdex of the inputted list
"""