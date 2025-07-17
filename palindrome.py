# Ask the user to input a word or phrase
text = input("Enter a word or number to check if it's a palindrome: ")

# Reverse the text
reversed_text = text[::-1]

# Compare original and reversed version
if text == reversed_text:
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")