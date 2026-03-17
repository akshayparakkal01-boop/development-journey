employees=["hari","dixon","joji"]
fw=open("nested_collection/nested_collection/files/employes.txt","w")
for e in employees:
    fw.write(e+"\n")
print("completed")




employees=["hari","dixon","joji"]
fw=open("nested_collection/nested_collection/files/employes.txt","a")
for e in employees:
    fw.write(e+"\n")
print("completed")