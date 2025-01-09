dictt ={
    'Monnei': 0,
    'Fjee': 0,
    'Dolladollabilljoll': 0
}

for i in dictt:
    ipt = int(input(' '))
    dictt[i] = ipt

for k,v in dictt.items():
    lowest_value = min(dictt.values())
    if lowest_value == v:
        lowest_key = k

print(lowest_key)   





dictt ={
    'Monnei': 0,
    'Fjee': 0,
    'Dolladollabilljoll': 0
}

for i in dictt:
    ipt = int(input(' '))
    dictt[i] = ipt
    
lowest_value = min(dictt.values())

'''
ה output הוא מפתח, רק במקרה שהערך שווה לערך הכי נמוך. 
'''
lowest_key = [key for key, value in dictt.items() if value == lowest_value][0]
print(lowest_key)



