fr=open("nested_collection/nested_collection/files/orders.txt","r")
all_orders=[line.rstrip("\n") for line in fr]
print(all_orders)
count_of_orders={o:all_orders.count(o) for o in all_orders}
print(count_of_orders)