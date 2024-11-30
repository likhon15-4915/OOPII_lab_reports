def update_salary(employee_dict, emp_id, new_salary): 
if emp_id in employee_dict: 
employee_dict[emp_id]['salary'] = new_salary 
print(f"Salary updated for employee ID {emp_id}") 
else: 
print(f"Employee ID {emp_id} not found") 
employee_details = { 
101: {'name': 'Alice', 'salary': 50000}, 
102: {'name': 'Bob', 'salary': 60000}, 
103: {'name': 'Charlie', 'salary': 55000} 
} 
emp_id_to_update = 102 
new_salary = 65000 
update_salary(employee_details, emp_id_to_update, new_salary) 
print("Updated employee details:") 
for emp_id, details in employee_details.items(): 
print(f"Employee ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}") 
