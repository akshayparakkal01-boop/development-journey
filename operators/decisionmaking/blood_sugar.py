fasting_blood_sugar=int(input("enter blood sugar:"))
if fasting_blood_sugar<100:
    print("normal")
elif fasting_blood_sugar<125:
    print("prediabets")
else:
    print("diabets")
    