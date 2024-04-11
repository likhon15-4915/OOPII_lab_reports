limit = int(input("Enter the limit for Fibonacci sequence: "))
a, b = 0, 1
for _ in range(limit):
 print(a, end=" ")
 a, b = b, a + b
