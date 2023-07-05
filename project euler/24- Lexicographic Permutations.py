import itertools
loop = 1
for i in itertools.permutations(range(0,9+1),):
    if loop ==1000000:
        print(*i)
        break
    else:
        loop+=1