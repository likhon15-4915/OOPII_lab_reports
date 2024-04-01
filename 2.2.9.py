def odd_sum(lst):
 if not lst:
 return 0
 elif lst[0] % 2 != 0:
 return lst[0] + odd_sum(lst[1:])
 else:
 return odd_sum(lst[1:])
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sum of odd numbers:", odd_sum(lst))
