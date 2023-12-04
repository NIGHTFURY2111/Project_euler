distinctTerms = set()
for a in range(2,100+1):
    for b in range(2,100+1):
        distinctTerms.add(a**b)
        
print(len(distinctTerms))