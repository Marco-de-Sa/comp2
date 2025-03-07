def letter_counter(s):
    ld = {}
    for i in range(len(s)):
        if s[i] not in ld:
            ld[s[i]] = 1
        else:
            ld[s[i]] = ld[s[i]] + 1
    return ld
w = input("Gimme a word: ")
letterDict = letter_counter(w.lower())
print(letterDict)