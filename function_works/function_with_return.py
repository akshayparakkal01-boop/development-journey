#function with parameter and return value
#if return used in function then only use print
def addition(num1,num2):
    result=num1+num2
    return result
print(addition(100,200))


#creat a function smart_sub with two parameters n,n2
#return subtraction result as n1-n2 if n1>n2 else return n2-n1
def smart_sub(n1,n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1
print(smart_sub(10,40))


#creat a function is_odd with parameter number return true if num is odd else return false

def is_odd(n1):
    if n1%2!=0:
        return True
    else:
        return False
print(is_odd(655))

#creat a function is_even with parameter number return true if num is even else return false
def is_even(n1):
    if n1%2==0:
        return True
    else:
        return False
print(is_even(85))

#creat a function is_positive with parameter number return true if num is positive else return false

def is_positive(n1):
    if n1>0:
        return True
    else:
        return False
print(is_positive(5))

#creat a function is_zero  with parameter number return true if num is zero else return false

def is_zero(n1):
    if n1==0:
        return True
    else:
        return False
print(is_zero(9))

def exponent(base,pow=2):
    result=base**pow
    return result
print(exponent(10,pow=3))


#creat a function calculator with n1,n2,op
#if op==+ return add of n1,n2
#if op==- return sub of n1,n2
#if op==* return mul of n1,n2
#if op==/ return div of n1,n2

def calculator(n1,n2,op="+"):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1*n2
    elif op == "/":
        return n1/n2
print(calculator(10,11,op="-"))    

    
