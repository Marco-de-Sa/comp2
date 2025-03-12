def fib(n, s, sn):
    if sn == n-2:
        return s[2:]
    s.append(s[sn] + s[sn+1])
    s = fib(n, s, sn+1)
    return s
    # print(s[2:])

numbers = int(input("till what n is the fib sequence"))
sNum = 0
start = [1, 1]
print(fib(numbers, start, sNum))