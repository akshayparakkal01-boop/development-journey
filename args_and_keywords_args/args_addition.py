"""
*args is used to pass arguments 
it receives value as tuple 
"""


def add(*args):
    return sum(args)
print(add(10,20))
def largest_number(*args):
    return max(args)
print(largest_number(1,7,42,87,44,75))

def count_even(*args):
    count=0
    for i in args:
        if i%2==0:
            count+=1
    return count
print(count_even(1,2,3,4,5,6,7,8))


def count_of_odd(*args):
    odd=[num for num in args if num%2!=0]
    return len(odd)
print(count_of_odd(1,2,3,4,5,6,7,8,9))







 