#B3.  Sensor Readings
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count_above = 0
highest = readings[0]
lowest = readings[0]
total = 0

for value in readings:
    if value > 3.2:
        count_above += 1
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value
    total += value

average = total / len(readings)

print("Readings above 3.2 V:", count_above)
print("Highest reading:", highest)
print("Lowest reading:", lowest)
print("Average reading:", average)
