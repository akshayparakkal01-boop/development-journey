number=int(input("enter number:"))
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if number==sum:
    print("perfect number")
else:
    print("not perfect number")