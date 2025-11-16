//aim:to write a sentence statistic program

//algorithm
Start
2. Input a sentence from the user.
3. Initialize counters:
words = 0
digits = 0
uppercase = 0
lowercase = 0
4. Split the sentence into words using split() and count them → words = len(sentence.split())
5. For each character in the sentence:
If the character is a digit → increment digits
If the character is uppercase → increment uppercase
If the character is lowercase → increment lowercase
6. Display the results: number of words, digits, uppercase, lowercase letters.
7. End

//program
sentence = input("Enter a sentence: ")
words = len(sentence.split())
digits = 0
uppercase = 0
lowercase = 0
for ch in sentence:
    if ch.isdigit():
        digits += 1
    elif ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
print("Number of words:", words)
print("Number of digits:", digits)
print("Number of uppercase letters:", uppercase)
print("Number of lowercase letters:", lowercase)
