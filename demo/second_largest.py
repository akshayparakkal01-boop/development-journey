lst=[10,11,12,13,15,17]
max=0
second_max=0
for num in lst:
    if num>max:
        second_max=max
        max=num
print(second_max)