import sys
n=int(input(''))
lst=[]
for x in range(1,n+1):
    data_set=input('').split(' ')
    lst.append(data_set)

for q in lst:
    summ=0
    q[1]=int(q[1])
    for i in range(q[1]):
        candels=i+2
        summ+=candels
    print(q[0],summ)
