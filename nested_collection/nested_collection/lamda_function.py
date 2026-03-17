"""
lamda_functions are functions which are anonymous and has single expression
syntax:

var_name=lambda p1,p2:expression
"""
#lambda_funtion

add=lambda num1,num2:num1+num2
sub= lambda num1,num2:num2-num1
cube= lambda num:num**3
print(add(1,2))
print(sub(3,4))
print(cube(3))

#normal function
def add(num1,num2):
    return num1+num2
print(add(1,2))


"""
odd even lambda function
"""
odd_even= lambda num: "even" if num%2==0 else "odd"

print(odd_even(9))
print(odd_even(4))

"""
number is positive
"""
is_positive= lambda num: True if num>0 else False
print(is_positive(-2))
