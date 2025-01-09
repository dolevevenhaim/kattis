n,k=input(' ').split(' ')
n=int(n)
k=int(k)
summ=0
for i in range(k):
    o=int(input(''))
    summ+=o
min_rating=(-3*(n-k)+summ)/n    
max_rating=(3*(n-k)+summ)/n    


print(min_rating,max_rating)

