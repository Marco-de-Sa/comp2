def lab_sorter(n, source, target, temp, counter):
    if n == 1:
        print(f"Move virus 1 from Lab {source} to Lab {target}")
        counter[0] += 1  # Increment counter
        return
    lab_sorter(n-1, source, temp, target, counter)
    print(f"Move virus {n} from Lab {source} to Lab {target}")
    counter[0] += 1  # Increment counter
    lab_sorter(n-1, temp, target, source, counter)

n = 4
counter = [0]
lab_sorter(n, 'A', 'B', 'C', counter)

# Total number of moves
print(f"Total moves: {counter[0]}")
# code from professor (not my code)