"""
METHOD OVERRIDE=child class redifines the method that is defined in parent class
"""
class Parent:
    def vehicle(self):
        print("gt 650")
    def vehicle(self):
        print("b6e")
class Child(Parent):
    def vehicle(self):
        print("harley davidson")
    def car(self):
        print("bmw")
child_instance=Child()
child_instance.vehicle()
child_instance.car()
