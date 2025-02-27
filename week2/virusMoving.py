lab_a = ["v5","v4","v3","v2","v1"]
lab_b = []
lab_c = []

def lab_sorting(n, a, b, c):
    if n == 1:
        c.append(a[-1])
        a.pop()
        # Move virus 1 from a to destination c
        return
    lab_sorting(n - 1, a, b, c)
    c.append(a[-1])
    a.pop()
    # Move virus n from a to destination c
    lab_sorting(n - 1, b, c, a)

n = len(lab_a)
lab_sorting(n, lab_a, lab_b, lab_c)