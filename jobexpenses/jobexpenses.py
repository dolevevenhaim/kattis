N=int(input(''))
K=list(map(int, input('').split(' ')))
flag=0
output=0
for i in K:
    if i>0:
        flag+=1
        if flag==len(K):
            output=0
    else:
        output+=abs(i)
print(output)        