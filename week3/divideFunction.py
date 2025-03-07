def divide_by(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error: divided by zero"
print(divide_by(int(input("input a: ")), int(input("input b: "))))