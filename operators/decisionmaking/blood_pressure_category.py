bp=int(input("enter systolic bp:"))
if bp<120:
    print("NORMAL")
elif bp<129:
    print("ELEVATED")
elif bp<139:
    print("HIGH BP STAGE 1")
elif bp>=140:
    print("HIGH BP STAGE 2")
    