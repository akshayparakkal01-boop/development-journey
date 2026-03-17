def product_num(*args:tuple):
    product=1
    for num in args:
        product*=num
    return product
print(product_num(10,20,30,40))
