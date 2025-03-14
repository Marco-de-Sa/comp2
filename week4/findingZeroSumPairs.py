from random import randint

inputted = [randint(-10, 10) for i in range(8)]
answers = []
usedValues = []
for i in inputted:
    for j in inputted:
        if i + j == 0 and not(i in usedValues or j in usedValues):
            answers.append((i, j))
            usedValues.append(i)
            usedValues.append(j)
print(answers)