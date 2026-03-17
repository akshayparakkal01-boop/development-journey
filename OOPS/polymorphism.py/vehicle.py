from abc import ABC,abstractmethod
class bike(ABC):
    @abstractmethod
    def transmission(self):pass
    @abstractmethod
    def start(self):pass

class gt650(bike):
    def transmission(self):
        print("6 speed manual transmission")
    def start(self):
        print("electric only starting system")
gt650_instance=gt650()
gt650_instance.start()
gt650_instance.transmission()

     
    