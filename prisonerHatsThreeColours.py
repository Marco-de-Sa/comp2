from random import randint

def first_two_prisoner(prisoners):
    hatCount = 0
    guesses = []

    # counts the amount of white hats infront of the second last prisoner
    for i in range(len(prisoners)-2):
        if prisoners[i] == 1:
            hatCount += 1
    if hatCount % 2 == 0:
        guesses.append("white")
    if hatCount % 2 == 1:
        guesses.append("black")
    
    # counts the amount of grey hats infront of the second last prisoner
    for i in range(len(prisoners)-2):
        if prisoners[i] == 2:
            hatCount += 1
    if hatCount % 2 == 0:
        guesses.append("grey")
    if hatCount % 2 == 1:
        guesses.append("black")
    return prisoner_guess(guesses, prisoners)

def prisoner_guess(guesses, prisoners):
    hatCountWhite = 0
    hatCountGrey = 0
    isEvenWhite = 0
    isEvenGrey = 0
    iterHat = 3
    whiteOrBlackOrGrey = "white"

    if guesses[0] == "white":
        isEvenWhite = 0
    elif guesses[0] == "black":
        isEvenWhite = 1

    if guesses[1] == "grey":
        isEvenGrey = 0
    elif guesses[1] == "black":
        isEvenGrey = 1

    for i in range(len(prisoners)):
        for j in range(len(prisoners) - iterHat):
            if prisoners[j] == 1:
                hatCountWhite += 1
        for j in range(len(prisoners) - iterHat):
            if prisoners[j] == 2:
                hatCountGrey += 1
        iterHat += 1
        if hatCountWhite%2 == isEvenWhite and hatCountGrey%2 == isEvenGrey:
            whiteOrBlackOrGrey = "black"
            guesses.append(whiteOrBlackOrGrey)
            if len(guesses) == len(prisoners):
                break
        elif hatCountGrey%2 != isEvenGrey:
            whiteOrBlackOrGrey = "grey"
            guesses.append(whiteOrBlackOrGrey)
            if isEvenGrey == 0:
                isEvenGrey = 1
            else:
                isEvenGrey = 0
            if len(guesses) == len(prisoners):
                break
        else:
            whiteOrBlackOrGrey = "white"
            guesses.append(whiteOrBlackOrGrey)
            if isEvenWhite == 0:
                isEvenWhite = 1
            else:
                isEvenWhite = 0
            if len(guesses) == len(prisoners):
                break
        hatCountWhite = 0
        hatCountGrey = 0
    return guesses

# 0 = black 1 = white 2 = grey
# randomises the list of prisoners where 0 represents a black hat and 1 represents a white hat and 2 represents grey
prisoners = [randint(0,2) for i in range(int(input("how many prisoners are there: ")))]
# prints the list of prisoners
print(prisoners)
# calls the first_prisoner function
print(first_two_prisoner(prisoners))
# testing