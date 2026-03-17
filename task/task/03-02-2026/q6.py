#⁠ ⁠Print the multiplication table of a given number using a for loop.
num=int(input("enter number:"))
for i in range(1,11):
    sum=num*i
    print(num,"x",i,"=",sum)