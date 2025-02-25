def count_down(num):
    if num == -1:
        print("boom")
        return ""
    elif num > -1:
        print(num)
        count_down(num-1)
    else:
        print("num not positive")

def sum_of(num):
    if num == 1:
        return num
    else:
        num += sum_of(num-1)
        return num

def power_of(a, b):
    num = a
    power = b
    if power == 0:
        return 1
    num *= power_of(num, power-1)
    return num

n = int(input("input a number for the countdown"))
print(sum_of(n))
print()
count_down(n)

print(power_of(2, 3))