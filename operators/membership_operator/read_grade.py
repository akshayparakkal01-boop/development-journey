grade=input("enter grade:")

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("good")
    case "C":
        print("average")
    case _:
        print("failed")
        