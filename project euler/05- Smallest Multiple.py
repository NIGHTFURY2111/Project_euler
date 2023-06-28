def primeList (UpperBound):
    list = [2]
    product = 2
    for i in range (2,UpperBound+1):
        Isprime= True
        for j in list:
            if i%j ==0:
                Isprime = False
                break
        if Isprime:    
            list.append(i)
    return list

upto = 20
lst=primeList(upto)
for i in range (len(lst)):
    temp = lst [i]
    while temp<upto:
        temp *= lst[i]
    temp/=lst[i]
    lst[i] = temp
print(lst) 
product = 1
for item in lst:
    product*=item
    
print(product)

