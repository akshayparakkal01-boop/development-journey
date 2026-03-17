"""
Cholesterol Level Check
Input: cholesterol
Conditions:
If cholesterol < 200 → Desirable
If cholesterol between 200 and 239 → Borderline High
If cholesterol ≥ 240 → High Cholesterol
"""
cholesterol=float(input("enter cholesterol:"))

if cholesterol<=200:
    print("Desirable")
elif cholesterol<=239:
    print("border line high:")
elif cholesterol>=240:
    print("high cholesterol")
    