"""
Daily Water Intake
Input: liters
Conditions:
If intake < 2 → Dehydrated
If intake between 2 and 3 → Adequate Intake
If intake > 3 → Excess Intake
"""
liters=float(input("enter liters:"))
if liters<2:
    print("Dehydrated")
elif liters>=2 and liters<=3:
    print("Adequate Intake")
else:
    print("Excess Intake")
    