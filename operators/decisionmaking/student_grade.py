mark1=int(input("enter mark 1:"))
mark2=int(input("enter mark 2:"))
mark3=int(input("enter mark 3:"))
total_mark=mark1+mark2+mark3
grace_mark=(2/100)*total_mark
final_mark=total_mark+grace_mark
if final_mark>=140:
    print("GRADE A")
elif final_mark>=130 and total_mark<=140:
    print("GRADE B")
elif final_mark>=120 and total_mark<=130:
    print("GRADE C")
elif final_mark<120:
    print("failed")
