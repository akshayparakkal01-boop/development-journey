"""
Write a program to determine exam result category.
•⁠  ⁠Marks ≥ 90 → Distinction
•⁠  ⁠Marks ≥ 60 → First class
•⁠  ⁠Marks ≥ 40 → Pass
•⁠  ⁠Below 40 → Fail
"""
mark=int(input("enter mark:"))
if mark>=90:
    print("distinction")
elif mark>=60:
    print("first class")
elif mark>=40:
    print("pass")
else:
    print("failed")
    