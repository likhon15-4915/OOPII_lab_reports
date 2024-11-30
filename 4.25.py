def print_student_details(student_dict): 
for student_id, details in student_dict.items(): 
print(f"Student ID: {student_id}") 
print(f"Name: {details['name']}") 
print(f"Age: {details['age']}") 
print(f"Address: {details['address']}") 
print() 
students = { 
1: {'name': 'Alice', 'age': 20, 'address': '123 Main St'}, 
2: {'name': 'Bob', 'age': 22, 'address': '456 Elm St'}, 
3: {'name': 'Charlie', 'age': 21, 'address': '789 Oak St'} 
} 
print_student_details(students) 
