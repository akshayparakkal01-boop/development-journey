class Biriyani:
    title:str
    category:str
    price:int
    
    def set_biriyani(self,title,category,price):
        
        self.title=title
        self.category=category
        self.price=price
    def display(self):
        print(self.title,self.category,self.price)
hydrabady_biriyani=Biriyani()

hydrabady_biriyani.set_biriyani("hydrabadhy biriyani og","chicken",230)