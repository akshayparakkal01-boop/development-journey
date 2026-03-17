def num_checker(*args,**kwargs):
    type=kwargs.get("type")
    if type=="odd":
        odd=[num for num in args if num%2!=0]
        return len(odd)
    elif type=="even":
        even=[num for num in args if num%2==0]
        return len(even)
    elif type=="negative":
        negative=[num for num in args if num<0]
        return len(negative)
    
    







print(num_checker(10,11,12,13,14,15,type="negative"))