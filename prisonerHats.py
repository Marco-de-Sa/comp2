from random import randint
#
def first_prisoner(prisoners):
    hatcount = 0
    prisoner_pos = len(prisoners)-1
    print(f"{prisoner_pos} first")

    for i in range(0, prisoner_pos):
        if prisoners[i] == 1:
            hatcount += 1

    prisoner_guess(prisoners, hatcount, prisoner_pos+1)
#

def prisoner_guess(prisoners, evenorodd, prisoner_pos):
    for i in range(prisoner_pos):
        hatcount = 0
        hatcounttemp = 0
        for j in range(0, prisoner_pos):
            if prisoners[i] == 1:
                hatcounttemp += 1

        if (hatcounttemp%2) != (hatcount%2):
            print("white")
        else:
            print("black")
        hatcount = hatcounttemp

# 0 = black 1 = white
prisoners = [randint(0,1) for i in range(5)]
print(prisoners)

first_prisoner(prisoners)