"""

set low =0
set upp=len(arr)-1
loop:
"""
arr=[10,11,12,13,14,15]
low=0
upp=len(arr)-1
element=int(input("enter element to search: "))
is_present=False
while low<=upp:
    mid=(low+upp)//2
    if element==arr[mid]:
        is_present=True
        break
    elif element<arr[mid]:
        upp=mid-1
    elif element>arr[mid]:
        low=mid+1
print(is_present)
