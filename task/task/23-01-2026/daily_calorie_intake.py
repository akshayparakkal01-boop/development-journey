"""
 Daily Calorie Intake
Input: calories
Conditions:
If calories < 1500 → Low Intake
If calories between 1500 and 2500 → Balanced Intake
If calories > 2500 → Excess Intake
"""
calorie=int(input("enter calorie:"))

if calorie<1500:
    print("Low Intake")
elif calorie>=1500 and calorie<=2500:
    print("Balance Intake")
else:
    print("Excess Intake")
