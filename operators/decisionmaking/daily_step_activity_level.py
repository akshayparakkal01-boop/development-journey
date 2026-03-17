step_conditions=int(input("enter number:"))
if step_conditions<5000:
    print("sedentary")
elif step_conditions>=5000 and step_conditions<=9999:
    print("moderately active")
elif step_conditions>=10000:
    print("Active")
