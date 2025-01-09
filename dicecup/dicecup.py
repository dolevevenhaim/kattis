import sys
n,m=map(int, input('').split(' '))
tmp_list=[]
dict={}

for x in range(1,n+1):
    for i in range(1,m+1):
        score=x+i
        tmp_list.append(score)
        counter=tmp_list.count(score)
        dict[score]=counter
# print(dict)

maxi=0
new_lst=[]
for k,v in dict.items():
    if v >= maxi:
        maxi=v
        output=k
        new_lst.append((output,maxi))
# print(new_lst)        
for q in new_lst:
    if q[1]==maxi:
        print(q[0])