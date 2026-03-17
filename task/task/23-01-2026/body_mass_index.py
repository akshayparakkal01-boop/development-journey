"""
Body Mass Index (BMI) Category
Input: bmi
Conditions:
If bmi < 18.5 → Underweight
If bmi between 18.5 and 24.9 → Normal Weight
If bmi between 25 and 29.9 → Overweight
If bmi ≥ 30 → Obese
"""
bmi=float(input("enter bmi:"))

if bmi<=18.5:
    print("underweight")
elif bmi<=24.4:
    print("Normal Weight")
elif bmi>=25 and bmi<=29.9:
    print("over weight")
else:
    print("obese")