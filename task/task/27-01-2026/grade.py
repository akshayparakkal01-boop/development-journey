grade=input("enter grade:")

match grade:
    case "a":
        print("excelent")
    case "b":
        print("good")
    case "c":
        print("above avarage")
    case "d":
        print("avarage")
    case _:
        print("failed")
