string=input('')
for i in string:
    if string.count(i)>1:
        output=0
        break
    else:
        output=1
print(output)        