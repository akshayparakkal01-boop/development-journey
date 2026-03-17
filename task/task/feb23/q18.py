"""
18. Remove multiple keys from a dictionary at once.

"""

stu_details = {"akshay":76,"srk": 46,"mohanlal":39,"mamooty":77}

keys_to_remove = {"akshay","srk"}
for k in keys_to_remove:
    del stu_details[k]
print(stu_details)