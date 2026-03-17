"""
attendance organize
H = "holiday"
P = "present"
o = "online"
"""
attendance=["H","P","P","P","P","O","H"]
for i in attendance:
    print(i)
print(attendance)


holiday_count=0
present_count=0
for att in attendance:
    if att == "H":
        holiday_count+=1
    elif att == "P":
        present_count+=1
print("holiday count", holiday_count)
print("present count", present_count)