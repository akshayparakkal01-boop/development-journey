db_roll_number=13

roll_number=int(input("enter roll number:"))
if db_roll_number==roll_number:
    mark=int(input("enter mark:"))
    if mark>=40:
        print("pass")
    else:
        print("failed")
else:
    print("roll number invalied")
