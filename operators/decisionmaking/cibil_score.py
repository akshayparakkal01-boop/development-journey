score=int(input("enter score"))
if score>=300 and score<550:
    print("poor")
elif score>=550 and score<650:
    print("average")
elif score>=650 and score<750:
    print("good")
elif score>=750 and score<900:
    print("excellent")
else:
    print("invalied")
    