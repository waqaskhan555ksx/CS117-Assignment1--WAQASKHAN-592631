#C2.  Parallel Resistance  
def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total += 1 / r
    return 1 / total


print("Equivalent resistance:", parallel_resistance([100, 100]), "ohm")
print("Equivalent resistance:", parallel_resistance([10, 20, 30]), "ohm")
