row=int(input(''))
lst=[]
for i in range(row):
    integer=int(input(''))
    if integer%2==0:
        lst.append((integer,' is even'))
    else:
        lst.append((integer,' is odd'))
        
for i in lst:
    print(i[0],i[1])
