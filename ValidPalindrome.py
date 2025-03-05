#Here I am using regula expression to remove all the special characters and spaces from the 
# string and then converting the string to lower case.

import re
def isPalindrome(s):
    s=re.sub(r'[^a-zA-Z0-9]','',s)
    s=s.lower()
    return s==s[::-1]

print(isPalindrome("ab_a"))
