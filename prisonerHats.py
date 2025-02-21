from random import randint

def first_prisoner(prisoners):
    hatCount = 0
    guesses = []

    # counts the amount of white hats infront of the last prisoner
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
    # iterHat records the space of the current prisoner
    iterHat = 2
    whiteOrBlack = "white"

    # sets the isEven variable to 0 if white was guessed indicating an even amount of white hats and 0 if not
    if guesses[0] == "white":
        isEven = 0
    elif guesses[0] == "black":
        isEven = 1

    # iterates through all the prisoners
    for i in range(len(prisoners)):
        # counts the number of hats infront of the prisoner
        for j in range(len(prisoners) - iterHat):
            if prisoners[j] == 1:
                hatCount += 1
        iterHat += 1
        # checks if the amount of white hats has changed since the last prisoner
        if hatCount%2 == isEven:
            # if the amount of white hats does not change it sets the current guess to black
            whiteOrBlack = "black"
            # appends the guess to the list of guesses
            guesses.append(whiteOrBlack)
            # breaks the for loop when the amount of guesses reaches the amount of prisoners
            if len(guesses) == len(prisoners):
                break
        else:
            # if the amount of white hats change it sets the current guess to white
            whiteOrBlack = "white"
            # appends the current guess to the list of guesses
            guesses.append(whiteOrBlack)
            # changes the isEven value since the amount of white hats are different
            if isEven == 0:
                isEven = 1
            else:
                isEven = 0
            # breaks the for loop when the amount of guesses reaches the amount of prisoners
            if len(guesses) == len(prisoners):
                break
        # resets the hat counter to 0
        hatCount = 0
    # prints the list of guesses
    print(guesses)

# 0 = black 1 = white
# randomises the list of prisoners where 0 represents a black hat and 1 represents a white hat
prisoners = [randint(0,1) for i in range(int(input("how many prisoners are there: ")))]
# prints the list of prisoners
print(prisoners)
# calls the first_prisoner function
first_prisoner(prisoners)
# testing