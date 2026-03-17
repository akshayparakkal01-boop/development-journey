class GrandParent:
    def properties(self):
        print("grand parents properties")
class Parent(GrandParent):
    def house(self):
        print("parent house method")
class child(Parent):
    pass
child_instance=child()
child_instance.house()
child_instance.properties()