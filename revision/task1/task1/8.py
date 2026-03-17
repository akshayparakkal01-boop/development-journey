number=int(input("enter number:"))
number_copy=number
digit_count=len(str(number))
result=0
while(number!=0):
    digit=number%10
    exponent=digit**digit_count
    result=result+exponent
    number=number//10
print(result)
if result==number_copy:
    print("amstring number")
else:
    print("not amstring number")

    