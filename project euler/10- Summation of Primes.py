Till = 2000000
Prime_List = [2,3]
sum = 5
for i in range (3, Till+1,2):
    if i%3 ==0:
        continue
    Isprime= True
    limit = int(i ** 0.5)+1
    for j in Prime_List:
        if j <= (limit):
            if i%j ==0:
                Isprime = False
                break
        else:
            break

    if Isprime:    
        Prime_List.append(i)
        sum +=i
        
print(len(Prime_List))
print(sum)