"""
number=1234
sum of digit=10
"""
number=int(input("enter number:"))
sum=0
while(number!=0):
    last_digit=number%10
    sum=sum+last_digit
    number=number//10
print(sum)
