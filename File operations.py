# Accept file name
filename = input("Enter file name: ")

try:
    file = open(filename, "r")

    # Display first N lines
    N = int(input("Enter number of lines: "))
    print(f"\nFirst {N} lines of the file:")
    for i in range(N):
        print(file.readline(), end="")

    # Count word frequency
    word = input("\n\nEnter word to search frequency: ")
    file.seek(0)
    content = file.read()
    words = content.split()
    count = words.count(word)

    print(f"\nFrequency of '{word}' is:", count)
    file.close()

except FileNotFoundError:
    print("File not found!")
