#B4. Continuous Discharge Analysis
voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

longest = 1
longest_start = 0
current = 1
current_start = 0

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current += 1
    else:
        current = 1
        current_start = i

    if current > longest:
        longest = current
        longest_start = current_start

longest_end = longest_start + longest - 1

print("Longest continuous drop:", longest, "minutes")
print("Started at:", voltages[longest_start], "V")
print("Ended at:", voltages[longest_end], "V")
