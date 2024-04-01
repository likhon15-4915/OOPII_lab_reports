def sum_digi(n):
 if n == 0:
 return 0
 else:
 return n % 10 + sum_digi(n // 10)
num = int(input("Enter a number: "))
print("Sum of digits:", sum_digi(num))
