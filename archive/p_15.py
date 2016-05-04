"""
Given a string find the minimum number of characters to be inserted for converting the string into a palindrome.
"""

def steps_to_palindrom(str):
    if len(str) < 2:
        return 0
    if str[0]==str[-1]:
        return steps_to_palindrom(str[1:-1])
    return 1+min( steps_to_palindrom(str[1:]) ,steps_to_palindrom(str[0:-1]))

print(steps_to_palindrom("ab"))
print(steps_to_palindrom("aab"))
print(steps_to_palindrom("abc"))
print(steps_to_palindrom("baab"))
print(steps_to_palindrom("bacdab"))
