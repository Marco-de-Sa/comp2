def converter(a):
    try:
        a = int(a)
        return a
    except:
        return "error: input not an int"
print(converter(input("Input: ")))