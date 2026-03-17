def skill_set(message):
    fr=open("error_handling/skill_sets.txt")
    skill_set=[line.strip()for line in fr]
    result=0
    for w in message.split(" "):
        if w in skill_set:
            result+=w+" "
    return result
print(skill_set("Python is a programing lamguage"))
