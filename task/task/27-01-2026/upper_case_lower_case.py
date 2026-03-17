char=input("enter character:")
asci_value=ord(char)

if asci_value in range(97,123):
    print("lower case")
 
elif asci_value in range(65,91):
    print("upper case")
else:
    print("no alphabet")
    