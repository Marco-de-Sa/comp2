lab_a = ["lab A","v5","v4","v3","v2","v1"]
lab_b = ["lab B"]
lab_c = ["lab C"]

def lab_sorting(n, a, c, b):
    if n == 1:
        if len(a) > 1:
            c.append(a.pop())
        # Move virus 1 from a to destination c
        return
    lab_sorting(n - 1, a, b, c)
    if len(a) > 1:
        c.append(a.pop())
    # Move virus n from a to destination c
    lab_sorting(n - 1, b, c, a)
    print(f"{a} {b} {c}")

n = len(lab_a)
lab_sorting(n, lab_a, lab_b, lab_c)

# non array version below

def lab_sorter(n, a, c, b):
    if n == 1:
        print("Move virus 1 from lab", a, "to lab", c)
        return
    lab_sorter(n - 1, a, b, c)
    print("Move virus", n, "from lab", a, "to lab", c)
    lab_sorter(n - 1, b, c, a)

n = 5
lab_sorter(n, 'A', 'B', 'C')