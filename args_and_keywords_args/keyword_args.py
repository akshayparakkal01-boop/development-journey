def employee_details(**kwar:dict):
    return kwar.get("name")
print(employee_details(name="mohanlal",dept="main character",salary=66000000))
