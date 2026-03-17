from csv import DictReader
fr=open("nested_collection/nested_collection/files/tips.txt")
data=list(DictReader(fr))
print(data[0])
day_wise_summary={}

for d in data:
    tip=float(d.get("tip"))
    day=d.get("day")
    if day in day_wise_summary:
        day_wise_summary[day]+=tip
    else:
        day_wise_summary[day]=tip
    print(day_wise_summary)


    day_wise_total={}
    for d in data:
        day=d.get("day")
        total_bill=float(d.get("total_bill"))
        if day in day_wise_total:
            day_wise_total[day]+=total_bill
        else:
            day_wise_total[day]=total_bill
        print(day_wise_total)