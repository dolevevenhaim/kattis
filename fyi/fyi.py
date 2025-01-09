import sys
t_number=input('')
lst=list(t_number)
if lst[0:3].count('5')==3 :
    print('1')
else:
    print('0')