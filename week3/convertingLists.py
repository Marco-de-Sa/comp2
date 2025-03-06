def convert_list(sl):
    cl = []
    for i in sl:
        try:
            cl.append(int(i))
            print(f"finished processing val: {i}")
        except ValueError:
            print(f"finished processing val: {i}")
            continue
    print(cl)

sList = [input("gimme a string to convert to an integer: ") for i in range(10)]
convert_list(sList)