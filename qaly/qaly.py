QALY=0

N=int(input(''))
for x in range(0,N):
     quality_of_life, number_of_years = map(float, input(' ').split())
     QALY+=quality_of_life*number_of_years
print(QALY)     