fr=open("nested_collection/nested_collection/files/food_logs.txt")
food_logs=[]
for line in fr:
    data=line.rstrip("\n").split(",")
    log={"id":data[0],"meal_type":data[1],"name":data[2],"calorie":data[3],"date":data[4],"owner":data[5]}
    food_logs.append(log)
print(food_logs)