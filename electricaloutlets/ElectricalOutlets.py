import sys
row=int(input(''))
for x in range(row):
    p_strip=input('').split(' ')
    remove_strip=p_strip.pop(0)
    new_list=list(map(int, p_strip))
    summ=sum(new_list)
    print(summ-len(new_list)+1)
    