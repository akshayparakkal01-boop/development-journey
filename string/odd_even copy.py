

"""
updated_stock_list=[15,16,17,18,19,20,25,26,27,28,29,30]
"""
stock_list1=[10,11,12,13,14,15]
stock_list2=[20,21,22,23,24,25]

compained_stock_list=[]
compained_stock_list.extend(stock_list1)
compained_stock_list.extend(stock_list2)

print(compained_stock_list)
updated_list=[]
for num in compained_stock_list:
    updated_list.append(num+5)
print(updated_list)