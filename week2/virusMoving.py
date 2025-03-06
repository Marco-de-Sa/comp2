lab_a = ["lab A","v6","v5","v4","v3","v2","v1"]
lab_b = ["lab B"]
lab_c = ["lab C"]

# opens a text file for purpose of counting how many moves have been made
file = open("count.txt", 'w')

def lab_sorting(n, a, c, b):
    if n == 1:
        # Move virus 1 from array a to c
        if len(a) > 1:
            # takes the top virus in the lab of list a and puts it in list a
            c.append(a.pop())
            # writes a placeholder text to the text file recording this move as a line
            file.write("a\n")
        return
    # switches labs in array b and c
    lab_sorting(n - 1, a, b, c)
    # Move virus n from array a to c
    if len(a) > 1:
        # takes the top virus in the lab of list a and puts it in list a
        c.append(a.pop())
        # writes a placeholder text to the text file recording this move as a line
        file.write("a\n")
    # shifts labs in arrays
    lab_sorting(n - 1, b, c, a)
# sets the n to the length of the lab_a array
n = len(lab_a)
# calls the lab_sorting function
lab_sorting(n, lab_a, lab_b, lab_c)

# opens the file in r so the amount of lines can be read
file = open("count.txt", 'r')

# reads the amount of lines in the text file and assigns it to the lines variable
lines = len(file.readlines())

# prints out the amount of movements to the command prompt
print('the amount of movements were:', lines)

# opens the file in w so we can use the truncate command
file = open("count.txt", 'w')

# truncates the file to 0
file.truncate()

# closes the file
file.close()

"""
test
"""

# instruction form of the problem
def lab_sorter(n, a, c, b):
    if n == 1:
        print("Move virus 1 from lab", a, "to lab", c)
        return
    lab_sorter(n - 1, a, b, c)
    print("Move virus", n, "from lab", a, "to lab", c)
    lab_sorter(n - 1, b, c, a)

lab_sorter(n, 'A', 'B', 'C')