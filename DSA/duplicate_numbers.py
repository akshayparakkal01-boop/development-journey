#find duplicate numbers without using any predefined methods

lst=[10,11,12,11,13,15,14,13]

lst.sort()
prev=0
next=prev+1
for prev in range(1,len(lst)-1):
    next=prev+1
    difference=lst[next]-lst[prev]
    if difference==0:
        print(lst[prev])


def find_duplicates(arr):
    arr.sort()
    next=prev+1
    difference=arr[next]-arr[prev]
    if difference==0:
        print(arr[prev])

arr=[10,11,12,11,13,14,13,15]