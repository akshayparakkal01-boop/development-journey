"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists
"""

student_details={"id":143,"name":"akshay","course":"data science","marks":98,"task":"ai"}

print(student_details["name"])

student_details["marks"]+=2
print(student_details)

student_details["grade"]="a"
print(student_details)

if "attendence" in student_details:
    print("yes")
else:
    print("no")