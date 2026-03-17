"""
Write a program to display day type based on day number.
•⁠  ⁠1–5 → Working day
•⁠  ⁠6–7 → Weekend

"""
day=int(input("enter day:"))

if day>=1 and day<=5:
    print("working day")
elif day>=6 and day<=7:
    print("weekend")
else:
    print("invalied")
    