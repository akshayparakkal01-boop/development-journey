month=input("enter month")
match month:
    case "jan"|"mar"|"july"|"aug"|"oct"|"dec":
        print(31)
    case "jun"|"apr"|"sep"|"nov":
        print(30)
    case "feb":
        print(28)
    case _:
        print("invalied")