from decimal import Decimal, getcontext
a,b=input().split()
getcontext().prec=1200
print("{0:f}" .format(Decimal(a)**int(b)))
