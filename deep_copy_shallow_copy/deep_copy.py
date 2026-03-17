from copy import deepcopy
akshay_food=[
    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"cb"},
    {"meal_type":"dinner","meal":"fried rice"}

]
srk_food=deepcopy(akshay_food)
srk_food[0]["meal"]="idly"

print("akshay",akshay_food)
print("srk",srk_food)