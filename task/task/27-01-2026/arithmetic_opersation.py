num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
print("1 → Addition")
print("2 → Subtraction")
print("3 → Multiplication")
print("4 → Division")
operation=int(input("enter operation:"))

match operation:
    case "+":
        print(num1,"+",num2,"=",add)
    case "-":

        print(num1,"-",num2,"=",subtract)
    case "*":

        print(num1,"*",num2,"=",multiplication)
    case "/":
        print(num1,"/",num2,"=",division)
    case _:
        print("invalied")
