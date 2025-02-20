from random import randint
#
def first_prisoner(prisoners):
    evenorodd = 0
    prisoner_pos = len(prisoners)-1
    for i in range(0, prisoner_pos):
        if prisoners[i] == 1:
            evenorodd += 1
    if evenorodd % 2 == 0:
        prisoner_guess(prisoners, 1, prisoner_pos+1)
    else:
        prisoner_guess(prisoners, 0, prisoner_pos+1)
#
#
def count_white(prisoners, prisoner_pos):
    evenorodd = 0
    for i in range(0, prisoner_pos):
        if prisoners[i] == 1:
            evenorodd += 1
    prisoner_pos -= 1
    if evenorodd % 2 == 0:
        return 1, prisoner_pos+1
    else:
        return 0, prisoner_pos+1
#

def prisoner_guess(prisoners, evenorodd, prisoner_pos):
    evenorodd2 = 0
    for i in range(prisoner_pos):
        evenorodd2, prisoner_pos = count_white(prisoners, prisoner_pos)
        if evenorodd != evenorodd2:
            print("white")
        elif evenorodd == evenorodd2:
            print("black")
        evenorodd = evenorodd2

# 0 = black 1 = white
prisoners = [randint(0,1) for i in range(5)]
print(prisoners)

first_prisoner(prisoners)