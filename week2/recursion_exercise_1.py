def count_down(num):
    if num == -1:
        print("boom")
        exit()
    elif num > -1:
        print(num)
        count_down(num-1)
    else:
        print("num not positive")

def sum_of(num):
    somVan = num
    if somVan == 0:
        return 0
    else:
        somVan += sum_of(num-1)

n = int(input("input a number for the countdown"))
print(sum_of(n))
print()
count_down(n)