"""
Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"
"""

bank_details={"ac_number":1234,"holder_name":"akshay","balance":120000000}

bank_details["balance"]+=5000
print(bank_details)

if bank_details["balance"]>2000:
    bank_details["balance"]-=2000
else:
    print("insufficient balance")

if bank_details["balance"]<1000 :
    print("low balance")

print(bank_details)