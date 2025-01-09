ches = {
    'One king': 1,
    'One queen': 1,
    'Two rooks': 2,
    'Two bishops': 2,
    'Two knights': 2,
    'Eight pawns': 8
}

my_input = input('').split(' ')

x=0
for key, value in ches.items():
    if x <= len(my_input):
        my_input = list(map(int, my_input))
        ches[key] = value - my_input[x]
    x+=1  

string_values = [f'{res}' for res in ches.values()]
joined_string = " ".join(string_values)
print(joined_string) 