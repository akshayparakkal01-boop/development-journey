def calculator(*args,**kwargs):
    if kwargs.get("key")=="+":
        return sum(args)
    if kwargs.get("key")=="*":
        product=1

        for num in args:
            product*=num
        return product
    if kwargs.get("key")=="-":
        dif=0
        for num in args:
            dif-=num
        return dif
    if kwargs.get("key")=="/":
        div=0
        for num in args:
            div/=num
        return div
    
print(calculator(10,20,30,40,key="*"))

