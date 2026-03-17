"""
Exercise Duration
Input: exercise_minutes
Conditions:
If minutes < 30 → Insufficient Exercise
If minutes between 30 and 60 → Good Exercise
If minutes > 60 → Intense Exercise
"""
exercise_minutes=int(input("enter minutes:"))
if exercise_minutes<30:
    print("Insufficient Exercise")
elif exercise_minutes>=30 and exercise_minutes<=60:
    print("good Exercise")
else:
    print("intense Exercise")
    