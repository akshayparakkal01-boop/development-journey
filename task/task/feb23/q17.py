"""
17. Merge two dictionaries. If duplicate keys exist, keep the higher value.

"""

stu_details = {"akshay":76,"mohanlal": 46,"mamooty":39,"srk":77}
employee_details = {"vijay":74,"surya": 56,"dq":19,"tovi":67}

for key in stu_details:

    if stu_details[key] == employee_details[key]:

        print