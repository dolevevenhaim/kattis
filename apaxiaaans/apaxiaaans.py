import sys
name=input('')
lst=[]
lst.append(name[0])
for x in range(1,len(name)):
    if name[x]==name[x-1]:
        continue
    else:
        lst.append(name[x])
new_lst=''.join(lst)        
print(new_lst)
