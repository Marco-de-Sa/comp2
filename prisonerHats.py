from random import randint

def first_prisoner(prisoners):
    hatCount = 0
    guesses = []

    # counts the amount of white hats
    for i in range(len(prisoners)-1):
        if prisoners[i] == 1:
            hatCount += 1
    # guesses white if there are an even amount of white hats and black if there are an uneven amount of white hats
    if hatCount % 2 == 0:
        guesses.append("white")
    if hatCount % 2 == 1:
        guesses.append("black")
    # parses the initial guesses
    prisoner_guess(guesses, prisoners)

def prisoner_guess(guesses, prisoners):
    hatCount = 0
    isEven = 0
    iterHat = 2
    if guesses[0] == "white":
        isEven = 0
    elif guesses[0] == "black":
        isEven = 1

    for i in range(len(prisoners) - iterHat):
        for j in range(len(prisoners) - iterHat):
            if prisoners[j] == 1:
                hatcount += 1
            iterHat += 1
        print(hatcount)
        hatcount = 0
        if hatCount%2 == isEven:
            guesses.append("black")
            isEven = 0
        else:
            guesses.append("white")
            isEven = 1
    print(guesses)




# 0 = black 1 = white
prisoners = [randint(0,1) for i in range(5)]
print(prisoners)
first_prisoner(prisoners)