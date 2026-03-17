def analyse_num(*args,**kwargs):
    if kwargs.get("key")=="max":
        return max(args)
    if kwargs.get("key")=="min":
        return min(args)
    if kwargs.get("key")=="count":
      return len(args)
print(analyse_num(10,11,12,13,14,15,key="max"))
print(analyse_num(10,11,12,13,14,15,key="min"))
print(analyse_num(10,11,12,13,14,15,key="count"))


