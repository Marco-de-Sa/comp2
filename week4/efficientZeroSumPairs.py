from random import randint

def find_zero_sum_pairs_optimized(lst):
    frequency = {}
    answers = []
    dupCheck = []
    frequency[lst[0]] = 1
    for i in lst[1:]:
        for j in frequency.keys():
            if j == i:
                frequency[j] += 1
            else:
                frequency[i] = 1
                break

    for i in frequency.keys():
        if -i in frequency and not(i in dupCheck or -i in dupCheck):
            answers.append((i, -i))
            dupCheck.append(i)
    return answers, frequency



inputted = [randint(-10, 10) for i in range(8)]
print(inputted)

answer, frequency = find_zero_sum_pairs_optimized(inputted)
print(answer)
print(frequency)