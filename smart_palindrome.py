## Is smart enough to ignore the following variation:

## Mixed upper and lower case: "Level" as well as "level" should be accepted as a palindrome.
## Space: "A Toyota" should be recognized as a palindrome.
## Punctuation: Allow commas, apostrophes, colons, and periods in the input string. That is, these all should test positive: "Madam, I'm Adam.", "A man, a plan, a canal: Panama."

import string

def check_smart_palindrome(x):
    s = x.lower().strip().translate(str.maketrans('', '', string.punctuation)).replace(" ","")
    bool_list = []
    for i in range(len(s)):
        if s[i] == s[len(s)-1-i]:
            bool_list.append(1)
    if len(bool_list) == len(s):
        print("YES, {} is a palindrome.".format(x))
    else:
        print("NO, {} is not a palindrome.".format(x))

exp = input("Give me a palindrome: ")

if len(exp) <= 2:
    print("Sorry, try something longer.")
else:
    check_smart_palindrome(exp)
