"""
Write a Python program to count how many times a loop runs when 
printing numbers from 1 to 20 using a while loop.

"""
count=0
i=1
while(i<=20):
    print(i)
    i=i+1
    count=count+1
print("loop rans for",count,"time")