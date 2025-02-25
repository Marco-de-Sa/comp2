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
    return sum_of(num-1)+num

n = int(input("input a number for the countdown"))
count_down(n)
print(sum_of(n))