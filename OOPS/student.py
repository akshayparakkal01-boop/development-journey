class Student:
    name:str
    course:str
    roll:int
    def __init__(self,name,course,roll):
        self.name=name
        self.course=course
        self.roll=roll
    def display(self):
        print(self.name,self.course,self.roll)



akshay_instance=Student("akshay","engineering",13)
mohanlal_instance=Student("mohanlal","actor",68)



akshay_instance.display()
mohanlal_instance.display()





