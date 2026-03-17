"""
Restaurant Order System

Task:
- Ask for table number

If table exists:
    - Ask for food availability
    - If food available:
        "Order placed"
    - Else:
        "Item out of stock"
Else:
    "Invalid table number"
"""
selected_table_number=7
menu="cb"
table_number=int(input("enter table number:"))
if table_number==selected_table_number:
    order=input("enter order:")
    if order==menu:
        print("order placed")
    else:
        print("iteam out of stock")
else:
    print("invalied table number")
