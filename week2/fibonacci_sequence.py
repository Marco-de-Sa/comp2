def fib(n, s, sn):
    # this if statement detects whether the function is at its end
    if sn == n-2:
        return s[2:]
    # appends the sum of the previous two values to the last spot in the list
    s.append(s[sn] + s[sn+1])
    # calls the function again and makes the result equal to the returned value
    s = fib(n, s, sn+1)
    # returns the list s after all the recursions are done
    return s

# asks the user how long they would like the sequence to be
numbers = int(input("till what n is the fib sequence"))
# sets the starting index of the sequence
sNum = 0
# sets the initial list for the sequence
start = [1, 1]
# parses the variables into the fib function
print(fib(numbers, start, sNum))