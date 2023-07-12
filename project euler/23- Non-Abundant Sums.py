import itertools
list = []
ambi_nums = []
# num_list=[i for i in range(28123)]
num_list = [1]

for i in range(2,28123):
    temp = [1]
    for j in range (2,i):
        if j in temp:
            break
        x,y = divmod(i,j)
        if y ==0:
            temp.append(j)
            if x not in temp:
                temp.append(x)
    
    if sum(temp) > i:
        list.append(i)
    
    isSum = False
    for j in list[:int(len(list)/2)]:
        diff = i-j
        
        if diff in list:
            isSum = True
            break
        
    if not isSum :
        num_list.append(i)



print(sum(num_list))

print(len(list))

