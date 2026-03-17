db_password="akshay123"
db_otp="3212"

user_password=input("enter password:")

if db_password==user_password:
   user_otp=input("enter otp")

   if user_otp==user_otp:
      print("login success")
   else:
      print("incorrect otp")
else:
   print("incorrect password")
