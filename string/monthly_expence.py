"""
jan-dec
year expence
"""

expenses=[24000,22000,31000,23500,48000,22210,23400,26000,23020,76050,11000,32500]
sum=0
for ex in expenses:
    print(ex)
    sum+=ex
print("yearly expense",sum)
avg=sum/12
print("avg expence",avg)