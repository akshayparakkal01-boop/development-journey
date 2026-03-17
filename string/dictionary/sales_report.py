sales_report={
    "sun":23000,
    "mon":16000,
    "tue":18000,
    "wed":15000,
    "thu":19000,
    "fri":19000,
    "sat":20000,
}
#display day wise sales
for key in sales_report:
    print(key,sales_report[key])

#total sale 
total_sale=0
for key in sales_report:
    sale=sales_report[key]
    total_sale+=sale
print(total_sale)

#avg_sale
avg_sale=total_sale/len(sales_report)
print(avg_sale)

for key in sales_report:
    value=sales_report[key]

if sales_report[key]<avg_sale:
    print(key,sales_report[key])
  