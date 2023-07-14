from itertools import permutations

print([ i for loop, i in enumerate(permutations(range(0,10))) if loop == 1000000])