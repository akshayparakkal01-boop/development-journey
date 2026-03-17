class Language:
    def __init__(self,l_name):
        self.l_name=l_name
    def display(self):
        print(self.l_name)
class FrameWork(Language):
    def __init__(self,l_name,name):
        super().__init__(l_name)
        self.name=name
    def display(self):
        super().display()
        print(self.name)
frameWork_instance=FrameWork("python","django")
frameWork_instance.display()

    