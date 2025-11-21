class Palindrome:
    def check(self, value):
        value = str(value)
        return value == value[::-1]

class StringPalindrome(Palindrome):
    pass

class IntegerPalindrome(Palindrome):
    pass

# Testing
s = StringPalindrome()
i = IntegerPalindrome()

print("String Palindrome Check:")
print("madam:", s.check("madam"))
print("hello:", s.check("hello"))

print("\nInteger Palindrome Check:")
print("121:", i.check(121))
print("456:", i.check(456))
