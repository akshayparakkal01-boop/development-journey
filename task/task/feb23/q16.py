"""
16. Write a program to safely access a key from a dictionary without causing an error if the key does not exist.

"""

stu_details = {"akshay":76,"mohanlal": 46,"mamooty":39,"srk":77}
print(stu_details.get("edwin","Key doesn't exist"))