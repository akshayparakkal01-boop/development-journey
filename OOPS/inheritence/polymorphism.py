#clear method overloading python def poly
#METHOD OVERLOADING =with same class name and same method name with deifferent parameters 


class Calculator:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
cal_instance=Calculator()
print(cal_instance.add(10,20,30,40))
print(cal_instance.add(100,200,300))
print(cal_instance.add(1000,2000))