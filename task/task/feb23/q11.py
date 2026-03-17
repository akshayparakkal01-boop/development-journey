"""
11. Create a dictionary of student names and marks. Print students who scored above 75.
"""
stu_details = {"akshay":76,"mohanlal": 46,"mamooty":39,"srk":77}
for key,value in stu_details.items():
    if value > 75:
        print(key)