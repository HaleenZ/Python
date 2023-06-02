string = input("Enter a string: ")

# Remove any whitespace and convert to lowercase
string = string.replace(" ", "").lower()

# Reverse the string
reversed_string = string[::-1]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
