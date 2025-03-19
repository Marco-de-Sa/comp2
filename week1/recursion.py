def factorial(n):
    # Returns the factorial of n using a recursive approach .
    if n == 0:
        return 1
    else :
        return n * factorial( n - 1)

print(factorial(4))