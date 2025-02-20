from random import randint

def first_prisoner(prisoners):
    evenorodd = 0
    prisoner_pos = len(prisoners)-1
    for i in range(0, prisoner_pos):
        if prisoners[i] == 1:
            evenorodd += 1
    if evenorodd % 2 == 0:
        prisoner_guess("even", prisoner_pos+1)
    else:
        prisoner_guess("odd", prisoner_pos+1)

def count_white(prisoner, prisoner_pos):
    evenorodd = 0
    for i in range(0, prisoner_pos):
        if prisoners[i] == 1:
            evenorodd += 1
    prisoner_pos += 1

def prisoner_guess(evenorodd, prisoner_pos):
    print()

# 0 = black 1 = white
prisoners = [randint(0,1) for i in range(5)]
print(prisoners)

first_prisoner(prisoners)