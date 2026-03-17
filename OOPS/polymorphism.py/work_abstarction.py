from abc import ABC,abstractmethod

class Editor:
    @abstractmethod
    def open(self):pass
    @abstractmethod
    def execute(self):pass
    @abstractmethod
    def debug(self):pass
class Vscode(Editor):
    def open(self):
        print("vs code open")
    def execute(self):
        print("vs code execute")
    def debug(self):
        print("vs code debug")
vs_code_inst=Vscode()
vs_code_inst.open()
vs_code_inst.execute
vs_code_inst.debug
