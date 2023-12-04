numList = [i for i in range(1,(1001*1001)+1)]
toAdd = [1]
index = 2
for i in range (1, 1001-1,2):
    for j in range (4):
        index +=i
        toAdd.append(numList[index-1])
        index+=1
        
print(sum(toAdd))