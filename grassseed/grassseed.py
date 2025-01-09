import sys
t_size=float(0)
t_price=float(0)
c=float(input(''))
l=int(input(''))
for x in range(0,l):
    w,h=map(float,input('').split(' '))
    size=w*h
    price=size*c
    t_price+=price
print(round(t_price,8))   