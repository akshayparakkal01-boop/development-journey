"""
class tuple:
   def count(self,value)
   def index(self,value)

"""
prices=(200,300,400,300)

print(prices.count(300))

print(prices.index(200))


"""
create a tuple and store your age only
"""
age=(20,)
print(type(age))



"""
colors list set()

"""
colors={"red","green","blue","blue","yellow","hai"}
for c in colors:
    print(c)




st={10,20,30,40,40,40}

for num in st:
    print(num)


"""
class set:
   def add(self,value)
"""
foods={"dosa","tea","cofee","fried rice"}
foods.add("biriyani")
print(foods)






"""
def set:
   union
   intersection
   difference
"""

set_a={10,20,30,40,50}
set_b={40,50,400,500,600}

u_set=set_a.union(set_b)
in_set=set_a.intersection(set_b)
diff_set=set_a.difference(set_b)
diff_set2=set_b.difference(set_a)

print(u_set)
print(in_set)
print(diff_set)
print(diff_set2)




print(set_a.issuperset(set_b))
print(set_b.issubset(set_a))

in_set=set_a.intersection(set_b)
print(in_set)