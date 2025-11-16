//aim: to check palindrome and count digit occurences

//algorithm
Step 1: Start
Step 2: Input a number from the user
Step 3: Convert the number to a string
Step 4: Reverse the string
Step 5: Compare original string with reversed string
If both are same → number is palindrome
Else → not palindrome
Step 6: Create a dictionary (or array) to count digit occurrences
Step 7: Traverse each digit in the number
Increase its count in the dictionar
Step 8: Display whether the number is palindrome
Step 9: Display the digit occurrence count
Step 10: Stop

//program
num = input("Enter a number: ")
if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
digit_count = {}     
for digit in num:
    if digit in digit_count:
        digit_count[digit] += 1
    else:
        digit_count[digit] = 1
print("Digit Occurrences:")
for digit, count in digit_count.items():
    print(f"Digit {digit} occurs {count} time(s)")
