## Same as smart_palindrome.py but That is, make it loop back until the user has given a palindrome. Start from the last script and build in a looping mechanism.


boolean = 0

import string

def check_smart_palindrome2(x):
    s = x.lower().strip().translate(str.maketrans('', '', string.punctuation)).replace(" ","")
    bool_list = []
    for i in range(len(s)):
        if s[i] == s[len(s)-1-i]:
            bool_list.append(1)
    if len(bool_list) == len(s):
        print("YES, {} is a palindrome.".format(x))
        print("Goodbye.")
        global boolean
        boolean = 1
    else:
        print("NO, {} is not a palindrome.".format(x))
        
# pal_loop.py

while boolean == 0:
    if boolean==1:
        break
        
    exp = input("Give me a palindrome: ")

    if len(exp) <= 2:
        print("Sorry, try something longer.")
    else:
        check_smart_palindrome2(exp)
