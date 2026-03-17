num1=int(input("enter number:"))
num2=int(input("enter number:"))
if num1<num2:
    smallest=num1
else:
    smallest=num2
gcd=1
for i in range(1,smallest+1):
    if num1%1==0 and num2%i==0:
        gcd=i
    print(gcd)