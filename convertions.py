//aim:to convert binary,octal to decimal, hexadecimal

//algorithm
Start
2. Define a function bin_to_dec(binary)
3. Initialize decimal = 0
4. Traverse each digit from left to right
5. For each digit, update
decimal = decimal * 2 + digit
6. Return decimal
7. End

//program
def bin_to_dec(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal
def oct_to_hex(octal):
    decimal_value = int(octal, 8)      
    hex_value = hex(decimal_value)[2:]
    return hex_value.upper()
print("1. Binary to Decimal")
binary = input("Enter a binary number: ")
decimal_output = bin_to_dec(binary)
print("Decimal Value:", decimal_output)

print("\n2. Octal to Hexadecimal")
octal = input("Enter an octal number: ")
hex_output = oct_to_hex(octal)
print("Hexadecimal Value:", hex_output)
