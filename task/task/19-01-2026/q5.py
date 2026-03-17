p=100000
r=10/12/100
n=12
f1=p*r*(1+r)**n
f2=(1+r)**n-1
emi=f1/f2

print("EMI Amount:",emi)
