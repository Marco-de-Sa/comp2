"""
Create a functioning calculator that prompts the user for two values and
an operator between +, -, * and /.
• Verify if the values can be converted to numbers and that the operator
is valid. Do not allow division by zero!
• If an exception occurs, print a message.
– Bonus points if you detect the specific type of error that occurred.
• If everything is alright, print the result.
• At the end, thank the user for using your calculator.
"""
try:
    a, b = int(input("Value a: ")), int(input("Value b: "))
except ValueError:
    print("one value not an int")
    print("thanks for using this calculator")
    exit()

s = input("input operator(+, -, *, /")
if s.strip() == "+":
    print(a+b)
elif s.strip() == "-":
    print(a-b)
elif s.strip() == "*":
    print(a*b)
elif s.strip() == "/":
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("thanks for using this calculator")