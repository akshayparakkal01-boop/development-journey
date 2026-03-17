oxygen_level=int(input("enter oxygen level:"))
if oxygen_level>=95:
    print("NORMAL")
elif oxygen_level>=94:
    print("MILD CONCERN")
elif oxygen_level<90:
    print("CRITICAL")
    