

prev=0
current=1
print(prev,current)
for i in range (1,16):
    next=prev+current
    print(next,end=" ")
    prev=current
    current=next


