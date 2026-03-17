"""
create a dictionary of product with attribute
id,title,price,avl_qty
"""

product={"id":1234,"title":"movie_ticket","price":200,"avl_qty":300}

print(product["title"])

product["avl_qty"]+=10
print(product)

#code:kathi

product["code"]="kathi"
print(product)


#chk key exist or not

if "offer" in product:
    print("yes")
else:
    print("no")