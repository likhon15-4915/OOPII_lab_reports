N = int(input("Enter a number: "))
sum_even = 0
i = 2
while i <= N:
 sum_even += i
 i += 2
print(f"Sum of even numbers up to {N}: {sum_even}")
