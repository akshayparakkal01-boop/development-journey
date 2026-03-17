"""
ATM Withdrawal
Task:
Ask for PIN.
If PIN is correct:
Ask for withdrawal amount
If amount ≤ balance → "Withdrawal successful"
Else → "Insufficient balance"
Else → "Incorrect PIN"
"""
db_pin=1234
db_balance=3000

user_pin=int(input("enter user atm pin:"))

if db_pin==user_pin:
    amount=int(input("enter withdrawal amound:"))
    if amount<=db_balance:
        print("withdrawal successfull")
    else:
        print("insufficient balance")
else:
    print("incorrect pin")
