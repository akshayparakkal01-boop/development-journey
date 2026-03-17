"""
W.A.P to create two list positive_list,negative
"""
numbers=[-1,-2,10,11,12,13,-13,-15,4,5,0]
positive_list=[]
negative_list=[]
for num in numbers:
    if num>0:
        positive_list.append(num)
    elif num<0 :
        negative_list.append(num)
    else:
        print(num,"zero")
print("negative numbers",negative_list)
print("positive number",positive_list)


"""
W.A.P creat two list square_list and cube_list
"""
numbers=[1,2,3,4,5,6,12,21,14,13,6,7]
sq_list=[]
cube_list=[]


for num in numbers:
    sq_list.append(num**2)
    cube_list.append(num**3)

print("sq",sq_list)
print("cube",cube_list)


"""
updated_stock_list=[15,16,17,18,19,20,25,26,27,28,29,30]
"""
stock_list1=[10,11,12,13,14,15]
stock_list2=[20,21,22,23,24,25]

compained_stock_list=[]
compained_stock_list.extend()
