def get_grade(percentage):
 if percentage >= 90:
 return "A+"
 elif 80 <= percentage <= 89:
 return "A"
 elif 70 <= percentage <= 79:
 return "B"
 elif 60 <= percentage <= 69:
 return "C"
 else:
 return "Fail"
percentage = float(input("Enter student's percentage: "))
grade = get_grade(percentage)
print(f"The student's grade is: {grade}")
