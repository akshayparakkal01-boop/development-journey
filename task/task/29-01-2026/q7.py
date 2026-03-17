num=int(input("enter number:"))#123
reverse_number=0#
while(num!=0):#
    last_digit=num%10#3
    reverse_number=reverse_number*10+last_digit#
    num=num//10#
print(reverse_number)#
