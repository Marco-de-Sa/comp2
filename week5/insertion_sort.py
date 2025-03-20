from random import randint

def insertion_sort(arr):
    cc = 0
    cs = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                cs += 1
                continue
            cc += 1
    print(f"checked: {cc}")
    print(f"swapped: {cs}")
    print(arr)

A = [randint(0,10) for i in range(10)]
print(A)

insertion_sort(A)