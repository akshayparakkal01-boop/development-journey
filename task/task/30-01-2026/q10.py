"""
 ⁠Write a program to find the sum of digits of a given number using a while loop.
"""
num=int(input("enter number:"))
sum=0
while (num!=0):
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print(sum)
