fr=open("nested_collection/nested_collection/files/flight_data.txt")
flight=[]
for line in fr:
    data=line.rstrip("\n").rsplit(",")
    passenger_data={"year":data[0],"month":data[1],"passangers":int(data[2])}
    flight.append(passenger_data)
    year_wise_count={}
    for p in flight:
        year=p.get("year")
        p_count=p.get("passangers")

if year in year_wise_count:
    year_wise_count[year]+=p_count
else:
    year_wise_count[year]=p_count

print(year_wise_count)
year_wise_count_sorted=sorted(year_wise_count,key=year_wise_count.get)
print(year_wise_count_sorted)