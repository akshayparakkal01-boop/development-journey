# lst=[10,11,12,13,14,15]
# map_square=lst(map(lambda n:n**2,lst))
# print(map_square)
# com_square=[num**2 for num in lst]
# print(com_square)





lst=[10,11,12,13,14,15]
evens=list(filter(lambda n:n%2==0,lst))
print(evens)
even_com=[num for num in lst if num%2==0]
print(even_com)