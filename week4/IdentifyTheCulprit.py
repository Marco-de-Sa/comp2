from random import randint

def bin_search(ser, bin_sel, sel_num):
    if 1 in ser[:sel_num] and not (len(sel_num) == 1 and (1 in ser[sel_num:] or 1 in ser[:sel_num])):
        bin_search(ser, bin_sel, sel_num//2)
    elif 1 in ser[sel_num:] and sel_num <= bin_sel//2 and not(len(ser(sel_num)) == 1 and (1 in ser[sel_num:] or 1 in ser[:sel_num])):
        bin_search(ser, bin_sel, bin_sel//2 + sel_num//2)
    else:
        return

server = [0, 0, 0, 0, 0, 0]
server[randint(0,5)] = 1
attempts = 0
binarySection = len(server)//2

bin_search(server, len(server), len(server)//2)