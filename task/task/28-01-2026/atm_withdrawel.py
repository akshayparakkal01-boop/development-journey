db_pin=6070
db_balance=3000

user_pin=int(input("enter pin:"))

if db_pin==user_pin:
    amount=int(input("enter amound:"))
    if amount<db_balance:
        print("withdrawel successful")
    else:
        print("insuficient balance")

else:
    print("incorrect pin number")
