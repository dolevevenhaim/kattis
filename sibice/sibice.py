N,W,H=map(int, input('').split(' '))
for i in range(N):
    o=int(input(' '))
    calc=(W**2+H**2)**0.5
    if o <= calc:
        print("DA")
    else:
        print('NE')
