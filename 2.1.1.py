def rotate_char(string, n):
 rotated_string = string[-n:] + string[:-n]
 return rotated_string
m = int(input("Size of String m: "))
input_string = input("Input String (without whitespace): ")
n = int(input("Number of characters to rotate: "))
if n <= m:
 secure_password = rotate_char(input_string, n)
 print("Secure Password:", secure_password)
else:
 print("Invalid input")
