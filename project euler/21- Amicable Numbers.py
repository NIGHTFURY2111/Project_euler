list = {}
ambi_nums = []

for i in range(1,10000):
    temp = []
    for j in range (1,i):
        if i%j ==0:
            temp.append(j)
    list[i] = sum(temp)
total = 0
for key, val in list.items():
    if val in list.keys() and list[val] == key and key !=val:
        ambi_nums.append(key)


print(sum(ambi_nums))