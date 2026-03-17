"""
string : sequence of character
create
variable_name = "test"
char='a'


"""
adress="""adress line """ #Sring
number=123 #int
is_active=True #boolien
avg=4.6 #float

"""
class str:
    def capitalize(self):
    def casefold(self)

"""
name="Luminar Technolab"
print(name.capitalize())
print(name.casefold())


"""
class str:
    def casefold()
    def capitalize(self)=return a capitillized version of string
    def index(self,substr)=return index of substr
    def count(self,substr):return number of time substring appears
"""

print(name.upper())
print(name.casefold())
print(name.index("Lu"))
print(name.find("Lu"))


word="luminar technolab technohub"

print(word.count("tech"))


"""
def isalpha():return true if str object is an alphabet
def isdigit():return true if str object is  digit
def isalnum():return true if str object is alphanumerical


"""

word="hello123"
print(word.isalpha())
print(word.isdigit())
print(word.isalnum())


"""
def startswith(self,prefix):return True if string starts with prefix
def endswith(self,suffix):return True if string starts with suffix

"""
word="luminar technolab"

print(word.startswith("lu"))#True
print(word.endswith("labs"))#False


"""
def
"""
word="   luminar technolab   "
print(word.strip())



"""
def strip(self)
def lstrip()
def rstip()
"""
word="\nluminar technolab\t"
new_word=word.lstrip("\n")
new_word=new_word.rstrip("\t")
print(new_word)



print(dir(str))


name="london"
print(name.index("on"))
print(name.find("on"))
print(name.rfind("on"))
