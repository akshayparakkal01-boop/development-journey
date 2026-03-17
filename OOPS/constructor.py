"""
constructor
special name python(__init__)
automatically invoked during object creation
initialize attributes of an instance
"""

class Mobile():
    def __init__(self,image,name,price,rating):
        self.image=image
        self.name=name
        self.price=price
        self.rating=rating
    def display(self):
        print(self.image,self.name,self.price,self.rating)
mobile_instance=Mobile("samsung galaxy S26.jpg","samsung galaxy S26",175000,4.5)
mobile_instance.display()
        