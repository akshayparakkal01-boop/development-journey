# error => zero division error
#        IndexError
#        FileNotFoundError
#        KeyError

age=int(input("enter age"))
if age<18:
    raise Exception("invalid age")
else:
    print("access granted")

#read a password
#if length of password is < 6 create a custom error ie password invalid

password=(input("enter password : "))
if len(password)<6:
    raise Exception("password invalied")
else:
    print("access granted")
    