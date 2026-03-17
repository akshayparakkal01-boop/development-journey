#Find the factorial of a number using a for loopnumber=int(input("enter number:"))
num=int(input("enter number:"))
i=1
result=1
while(i<=num):
    result=result*i
    i=i+1
print(num,"factorial is",result)