number=int(input("enter number:"))
number_copy=number
result=0
while(number!=0):
    digit=number%10
    result=result*10+digit
    number=number//10
if number_copy==result:
    print(number_copy,"is a palindrome")
else:
    print(number_copy,"is not a palindrome")
    