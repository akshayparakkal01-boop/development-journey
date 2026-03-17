def is_fibonacci_number(number):
    is_fibo=False

    prev=0
    current=1
    next=prev+current

    while(next<=number):
        next=prev+current
        prev=current
        current=next
        if next==number:
            is_fibo=True
            break
    return is_fibo
print(is_fibonacci_number(3))#True 
print(is_fibonacci_number(77))#false 

