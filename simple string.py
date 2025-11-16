//aim:to write a simple string similarity

//algorithm
Start
2. Input two strings → s1, s2
3. Convert both to lowercase
4. Count number of characters that match at the same position
5. Similarity = matches / max(len(s1), len(s2))
6. Print similarity
7. End

//program
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s1 = s1.lower()
s2 = s2.lower()
matches = 0
min_len = min(len(s1), len(s2))
max_len = max(len(s1), len(s2))
for i in range(min_len):
    if s1[i] == s2[i]:
        matches += 1
similarity = matches / max_len
print("String Similarity:", similarity)
