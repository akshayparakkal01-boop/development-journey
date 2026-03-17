manali={
    "dijo":300,
    "akshay":1000,
    "edwin":800,
    "alan":15000,
    "manoj":0,
    "subin":0,
    "sreeyesh":500,
}

total_expence=0
for val in manali.values():
    total_expence+=val
print(total_expence)

individual_split=round(total_expence/len(manali))
print(individual_split)

spend_wise={}
for k,v in manali.items():
    payment=individual_split-v
    spend_wise[k]=payment
print(spend_wise)