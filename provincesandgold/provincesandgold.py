G,S,C=map(int,input('').split(' '))
gold=G*3
silver=S*2
copper=C*1
total=gold+silver+copper

if total>=8:
    print('Province or ',end='')
elif 5<= total <8:   
    print('Duchy or ',end='')
elif 2 <= total <5:
    print('Estate or ',end='')

if total>=6:
    print('Gold')
elif 3<= total <6:   
    print('Silver')
else:
    print('Copper')  