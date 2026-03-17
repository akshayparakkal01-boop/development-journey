"""
Write a program to check temperature status.
•⁠  ⁠Below 20 → Cold
•⁠  ⁠20–30 → Normal
•⁠  ⁠Above 30 → Hot 

"""
temperature=int(input("enter temperature:"))
if temperature<20:
    print("Cold")
elif temperature>=20 and temperature<=30:
    print("normal")
else:
    print("hot")
    