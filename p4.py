# Sample List
sample_list = ['abc', 'xyz', 'aba', '1221']

# Count the number of strings
count = sum(1 for s in sample_list if len(s) >= 2 and s[0] == s[-1])
print(count)
