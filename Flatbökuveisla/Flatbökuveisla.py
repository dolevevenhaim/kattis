# qun_piz = int(input(''))
# qun_pep = int(input(''))
# res = qun_piz % qun_pep
# print(res)

def mod (qun_miz, qun_peop):
    results = qun_miz % qun_peop
    return results

results = mod(int(input('type num pf pizza: ')), int(input('type num pf persons: ')))
print(results)