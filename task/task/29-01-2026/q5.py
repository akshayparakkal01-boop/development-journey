"""
Write a Python program to print the multiplication table of a given number using a while loop.

"""
multiplier=int(input("enter number:"))
i=1
while(i<=10):
    product=multiplier*i
    print(multiplier,"x",i,"=",product)
    i=i+1