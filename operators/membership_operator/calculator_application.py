num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

operation=input("enter operation:")

match operation:
    case "add":
        print(num1+num2)
    case "subtract":
        print(num1-num2)
    case "multiplication":
        print(num1*num2)
    case "divition":
        print(num1/num2)
    case "mod":
        print(num1%num2)
    case "expo":
        print(num1**num2)
    case "floar":
        print(num1//num2)
    case _:
        print("invalied")
