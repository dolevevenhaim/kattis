H,M=map(int,input('').split(' '))
i=15
if M+i > 59:
    new_M=(M+i)-60
    new_H=H
else:    
    new_M=M+i
    new_H=H-1
if H==0:
    new_H=H+23
print(new_H,new_M)