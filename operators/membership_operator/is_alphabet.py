#print(Ord("a"))
#print(ord("b"))
#print(ord("z"))

char=input("enter character:")
asci_value=ord(char)

if asci_value in range(97,123) or asci_value in range(65,91):
    print("alphabet")
else:
    print("no alphabet")
    