def is_palindrome(s):
 x = len(s)-1
 for i in range(len(s)):
 if(s[i] != s[x]):
 return False
 x+=1
 if(x >= i):
 break
 return True
string = input("Enter a string: ")
if is_palindrome(string):
 print("The string is a palindrome.")
else:
 print("The string is not a palindrome.")
