"""
Write a program to calculate discount eligibility based on purchase amount.
•⁠  ⁠Above 5000 → 20% discount
•⁠  ⁠2000–5000 → 10% discount
•⁠  ⁠Below 2000 → No discount

"""
amount=int(input("enter amount:"))

if amount>=5000:
        print("20% Disscount")
elif (amount>=2000) and (amount<5000):
        print("10% Disscout")
else:
        
        print("NO Disscount")


