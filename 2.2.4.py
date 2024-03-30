def rev_int(num):
 rev_num = 0
 while num > 0:
 digit = num % 10
 rev_num = (rev_num * 10) + digit
 num //= 10
 return rev_num
number = int(input("Enter an integer number: "))
reversed_number = rev_int(number)
print("Reversed number:", reversed_number)
