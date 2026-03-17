limit=int(input("enter number:"))
i=1
odd_sum=0
even_sum=0
while(i<=limit):
    if i%2==0:
        even_sum=even_sum+i


    else:
        odd_sum=odd_sum+i


    i=i+1

print("sum of even number upto",limit,"is",even_sum)
print("sum of odd numbers upto",limit,"is",odd_sum)






