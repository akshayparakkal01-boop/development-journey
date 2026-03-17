"""
14. Create a dictionary from two lists (one list of keys and one list of values).
"""
lst1 = ["akshay","mohanlal","mammooty","srk"]
lst2 = [50,15,45,89]
final_dict = {}
for i in range(len(lst1)):
    final_dict[lst1[i]] = lst2[i]
print(final_dict)