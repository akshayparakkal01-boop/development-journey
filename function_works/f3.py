#last digit max
def last_digit_max(num1,num2):

    last_digit_num1=num1%10
    last_digit_num2=num2%10
    if last_digit_num1>last_digit_num2:
        print(f"last digit of {num1} is greater")
    else:
        print(f"last digit of {num2} is greater")

last_digit_max(1234,678)