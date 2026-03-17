#inheritage
#mechanism of child class accessing attributes and methods form parent class

class Parent:
    def house(self):
        print("parent class house method")
class Child(Parent):#Child class inherits Parent class so, Child class can access attributes and methods from Parent class
    def mobile(self):
        print("child class mobile method")
child_instance=Child()
child_instance.mobile()
child_instance.house()