all_students=open("nested_collection/nested_collection/files/all_students.txt","r")
pass_students=open("nested_collection/nested_collection/files/passed_students.txt","r")
fr_failed=open("nested_collection/nested_collection/files/failed_students.txt","w")

all_students_list=[line.rstrip("\n") for line in all_students]
pass_students_list=[line.rstrip("\n") for line in pass_students ]
print("all",all_students)
print("pass",pass_students)
failed_students=set(all_students_list).difference(pass_students_list)
print("failed",failed_students)
for name in failed_students:
    fr_failed.write(name+" ")