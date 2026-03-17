daily_calories={
    "sun":2000,
    "mon":2600,
    "tue":2300,
    "wed":2030,
    "thu":2001,
    "fri":3200,
    "sat":3000,
}

for key in daily_calories:
    print(key,daily_calories[key])

total_calories=0
for key in daily_calories:
    cal=daily_calories[key]
    total_calories+=cal

print(total_calories)
print(total_calories/len(daily_calories))