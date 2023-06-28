import itertools as it
def prime_calculator(length):
    global Prime_List
    for i in it.count(3,2):
        if i%3 ==0:
            continue
        if len(Prime_List) == length:
            break
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
            
Prime_List = [2,3]
prime_calculator(10022)
print(Prime_List[10000])