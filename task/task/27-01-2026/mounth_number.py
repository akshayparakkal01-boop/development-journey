"""
Write a program using match–case to display the month name based on the month number.

"""
mounth=int(input("enter mounth number:"))
match mounth:
    case 1:
        print("jan")
    case 2:
        print("feb")
    case 3:
        print("mar")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6 :
        print("june")
    case 7:
        print("july")
    case 8:
        print("aug")
    case 9:
        print("sep")
    case 10:
        print("oct")
    case 11:
        print("nov")
    case 12:
        print("dec")
    case _:
        print("invalied")


