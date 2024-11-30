ages_dict = { 
"Alice": 25, 
"Bob": 30, 
"Charlie": 20, 
"David": 35, 
"Eve": 28 
} 
sorted_ages = sorted(ages_dict.items(), key=lambda x: x[1]) 
sorted_dict = dict(sorted_ages) 
print("Sorted dictionary based on age in ascending order:") 
for name, age in sorted_dict.items(): 
print(f"{name}: {age} years old")
