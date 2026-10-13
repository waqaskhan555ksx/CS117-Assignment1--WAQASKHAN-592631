#B5. Resistor Tolerance Sorting 
tol1 = 0
tol5 = 0
reject = 0

value = float(input("Enter measured resistance (0 to stop): "))

while value != 0:
    if value >= 99.0 and value <= 101.0:
        tol1 += 1
    elif value >= 95.0 and value <= 105.0:
        tol5 += 1
    else:
        reject += 1
    value = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", tol1)
print("5% tolerance:", tol5)
print("Reject:", reject)
