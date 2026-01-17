decimal_num = int(input("Enter a positive decimal integer: "))
binary_num = ""
while decimal_num > 0:
    remainder = decimal_num % 2
    binary_num = str(remainder) + binary_num
    decimal_num //= 2
print(f"The binary representation is: {binary_num}")