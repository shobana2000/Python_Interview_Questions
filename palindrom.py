def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase
    s = ''.join(filter(str.isalnum, s))  # Remove non-alphanumeric characters
    return s == s[::-1]  # Compare the string with its reverse

# Input from the user
word = input("Enter a word: ")

if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")

##palindrom concept:

## words:                           ## Numbers:

# "radar"                               # 121
# "level"                               # 1331
# "deified"                             # 12321

## Phrases:

# "A man, a plan, a canal, Panama!"
# "Madam, in Eden, I'm Adam."

