students = {"Alice": {"math": 77, "English": 67}, "Bob": {"math": 45, "English": 56}, "John": {"math": 98, "English": 80}}
nStudent = {}
temp = 0
tempName = ""
for i in students.keys():
    for j in students[i].values():
        temp+= j
    temp = temp/2
    nStudent[i] = temp
    temp = 0
print(nStudent)

for i in students.keys():
    for j in students[i].values():
        if j > temp:
            temp = j
            tempName = i
print(f"{tempName}: {nStudent[tempName]}")