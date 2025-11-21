import re

# Open file and read content
file = open("sample.txt", "r")
text = file.read()

# Regular expressions for phone number and email
phone_pattern = r"\+?\d{10,13}"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

phones = re.findall(phone_pattern, text)
emails = re.findall(email_pattern, text)

print("Phone Numbers Found:", phones)
print("Email Addresses Found:", emails)

file.close()
