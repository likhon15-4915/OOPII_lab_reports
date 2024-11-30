def add_or_update_student_score(student_scores, student_name, new_score): 
if student_name in student_scores: 
student_scores[student_name] = new_score 
print(f"Score updated for {student_name}.") 
else: 
student_scores[student_name] = new_score 
print(f"Added {student_name} to the dictionary.") 
student_scores = { 
"Alice": 85, 
"Bob": 92, 
"Charlie": 78 
} 
add_or_update_student_score(student_scores, "David", 80) 
add_or_update_student_score(student_scores, "Bob", 95) 
print("Updated Student Scores:", student_scores)
