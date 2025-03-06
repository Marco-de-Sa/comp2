students = {"Alice" : 92 ,"Bob" : 78 ,"Charlie" : 55 ,"David" : 89 ,"Ed" : 42 ,"Frank" : 1}
st = {}

for i in students.keys():
    if students[i] >= 90:
        st[i] = "A"
    elif students[i] >= 70:
        st[i] = "B"
    elif students[i] >= 50:
        st[i] = "C"
    elif students[i] >= 30:
        st[i] = "D"
    elif students[i] >= 0:
        st[i] = "Horrible!"
print(st)