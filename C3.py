#C3.  Decimal to Binary   
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


print("10 in binary:", decimal_to_binary(10))
print("25 in binary:", decimal_to_binary(25))
print("255 in binary:", decimal_to_binary(255))
