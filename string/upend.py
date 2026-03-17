"""
class list:
def append(self,object)add object end of the list
def insert(self,index,object)insert new object at specified index
def pop (self,index=-1) remove and return specified element at index
def remove(self,object) remove first occurance of object
def count(self,object)frequency of object in this list
"""

colors=["red","green","blue"]
colors.append("black")
print(colors)

colors.insert(2,"yellow") #[r,g,y,b,b]
print(colors)

remove_element=colors.pop()
print(colors)

colors.remove("green")
print(colors)



new_colors=["red","green","blue","green","red","red"]

print(new_colors.count("red"))


"""
def copy
"""
ak_fav_colors=["red","white","blue","black"]
sree_fav_colors=ak_fav_colors.copy()
sree_fav_colors[0]="yellow"
print(sree_fav_colors)

print(ak_fav_colors is sree_fav_colors)
print(ak_fav_colors==sree_fav_colors)
print(ak_fav_colors is sree_fav_colors)


"""
def sort(self,reverse=false)

"""
numbers=[12,1,12,13,14,15]
numbers.sort(reverse=True)
print(numbers)
numbers.sort()
print(numbers)

"""
reverse the colors
"""
colors=["red","white","blue","black"]
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)

"""
def extend(self,iterable)

"""
colors=["red","white","blue","black"]
new_colors=["cyan","brown","purple"]
colors.extend(new_colors)
print(colors)