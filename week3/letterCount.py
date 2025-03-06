def letter_counter(s):
    ld = {}
    for i in range(len(s)):
        if s[i].lower() not in ld:
            ld[s[i].lower()] = 1
        else:
            ld[s[i].lower()] = ld[s[i].lower()] + 1
    return ld
w = input("Gimme a word: ")
letterDict = letter_counter(w)
print(letterDict)