from random import randint

server = [0, 0, 0, 0, 0, 0, 0]
server[randint(0,6)] = 1
attempts = 0
# planned: use binary search
binarySection = len(server)//2
if 1 in server[binarySection]:
    attempts+=1
else:
    binarySection += binarySection//2
    if 1 in server[binarySection]: