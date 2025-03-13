# This code will execute n prints
def print_elements(lst):
    for element in lst:
        print(element)

# While this one executes n^2 prints
def print_all_pairs(lst):
    for i in lst :
        for j in lst :
            print(i , j)
"""
input: [a, b, c]
output:
a a
a b 
a c
b a
b b
b c
c a
c b
c c
"""

# And this one will only execute a portion of n iterations .
def logarithmic_example(n):
    while n > 0:
        print(n)
        n //= 2 # Divide n by 2 and round down
"""
input: 20
output:
20
10
5
2
1
"""