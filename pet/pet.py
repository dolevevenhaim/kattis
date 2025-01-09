maxi=0
index=1
lst=[]
for i in range(1,6):
    usr_rate=sum(map(int,input('').split(' ',4)))
    if usr_rate>maxi:
        maxi=usr_rate
        index=i    
print(index,maxi)
