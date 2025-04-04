from random import randint

def bin_search(ser, pos_r, pos_l, area, differ):
    area = len(ser)//2
    if len(ser) == 1:
        return differ
    elif 1 in ser[area:]:
        if pos_r < len(ser[area:]):
            differ += len(ser[area:])
        return bin_search(ser[area:], pos_r, pos_l, area)
    elif 1 in ser[:area]:
        if len(ser[:area]) > pos_l:
            differ -= len(ser[:area])
        return bin_search(ser[:area], pos_r, pos_l, area)
server = [0, 0, 0, 0, 0, 0, 0, 0]
server[randint(0,7)] = 1
binarySection = len(server)//2
diff = bin_search(server, 0, 0, len(server), 0)
totalDiff = binarySection + diff
print(f"debug:({server})")
print(f"the index for the broken server is: {totalDiff}")
