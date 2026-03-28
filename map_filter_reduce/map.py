#map
#map is used apply function on every element present

list1=[1,2,3,4,5,8]
list2=[6,7,8,9,10]

addition=list(map(lambda x,y:x+y,list1,list2))
print(addition)


cube=list(map(lambda x:x**3,list1))

print(cube)