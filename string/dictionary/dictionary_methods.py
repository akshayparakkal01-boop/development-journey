"""
class dict:
   def keys(self):return all keys 
   def value(self): return all values
   def items(self):
   def get(self,key):
   def pop(self,key):
"""
employe={"id":101,"name":"hari","salary":54000,"dept":"qa"}

for key in employe.keys():
    print(key)
for val in employe.values():
    print(val)

for k,v in employe.items():
    print(k,v)

print(employe["name"])#if true return value , if false error
print(employe.get("name"))#if true return value ,if false None
print(employe.get("email","dummy@gmail.com")) #if true value returs, if false the second key returs

employe.pop("dept")
print(employe)