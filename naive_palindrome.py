## If the input string x is too short (0-2 characters long), print out: 'Sorry, try something longer.'
## Else, if x IS a palindrome, print out: 'YES, "x" is a palindrome.', where x is the input string.
## Otherwise, if x is NOT a palindrome, print out: 'NO, "x" is not a palindrome.'

def check_palindrome(s):
    bool_list = []
    for i in range(len(s)):
        if s[i] == s[len(s)-1-i]:
            bool_list.append(1)
    if len(bool_list) == len(s):
        print("YES, {} is a palindrome.".format(s))
    else:
        print("NO, {} is not a palindrome.".format(s))

exp = input("Give me a palindrome: ")

if len(exp) <= 2:
    print("Sorry, try something longer.")
else:
    check_palindrome(exp)
