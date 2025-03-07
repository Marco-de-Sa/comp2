def fib(n, s):
    if len(s) == 0:
        s.append(1)
        s.append(2)
        fib(n-1, s)
        print(s)
    else:
        s.append(s[n] + s[n-1])
        fib(n-1, s)

numbers = int(input("till what n is the fib sequence"))
start = []
fib(numbers, start)