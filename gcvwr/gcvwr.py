import sys
G,T,N= map(int, input('').split())
carrying_weight=G-T
total_weight=carrying_weight*0.9
summ=0
weight_iteams= input('').split(' ',N-1)
for x in weight_iteams:
    x=int(x)
    summ+=x
output=int(total_weight-summ)  
print(output)
