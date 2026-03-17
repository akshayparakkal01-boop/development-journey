age=int(input("enter age:"))

if age>=18:
    seat=int(input("enter seat:"))
    if seat<=5:
        print("Ticket booked")
    else:
        print("house full")
else:
    print("not eligible")
