"""
20. Convert a dictionary into a list of tuples.
"""
stu_details = {"akshay":76,"srk": 46,"mohanlal":39,"mamooty":77}
tup_list = []
for keys,values in stu_details.items():
    tup_list.append((keys,values))
print(tup_list)