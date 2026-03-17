"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""

lst = [1, 2, 3, 5]

"""
length=len(lst)
for i in range(1,length+1):
    if i not in lst:
        print(i,"is missing")
        break
else:
    print(length+1,"is missing")"""



lst.sort()

pre=0
next=pre+1
difference=next-pre
for i in range(len(lst)-1):

    if difference!=1:
        print(lst[pre]+1)



def missing_least_positive(arr):
    arr.sort()
    prev=0
    next=prev+1

    while(prev<=len(arr)-2):
        difference=arr[next]-arr[prev]
        if difference!=1:
            print(arr[prev]+1,"is missing")
            break
        prev+=1
        next+prev+1
missing_least_positive([1,2,4,5])



def missing_least_positive(arr):
    arr.sort()
    for pre in range(0,len(arr)-1):
        next=pre+1
        difference=arr[next]-arr[pre]
        if difference!=1:
            print(arr[pre]+1,"is missing")
            break
    else:
        print(arr[-1]+1)
missing_least_positive([1,3,4,5])

