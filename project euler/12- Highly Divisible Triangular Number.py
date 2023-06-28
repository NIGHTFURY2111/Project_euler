import numpy as np
import itertools as it
def prime_calculator(Till):
    global Prime_List
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
         
Prime_List = [2, 3]

# n*(n+1)/2
n = 0
fact=[]
lst =[]
x= 12370
for i in it.count(1):
    n+=i
    # lst.append(n)
    if i ==12370:
        break
prime_calculator(100)
# lst = lst[1000:]
n = x*(x+1)/2
for iter in it.count(12370+1):
    n+=iter
    i=n
    # if not(i %6 == 0 and i%5 == 0) :
    #     continue
    fact= []
    while i >1:
        flag = False
        for j in Prime_List:
            if not(i%j == 0):
                flag = True
                break
            temp= []
            # if j>i:
            #     break
            # else:
            while i%j ==0:
                temp.append(j)
                i= i/j
            fact.append(len(temp)+1)
            if i ==1:
                break
        if flag:
            break
    if flag:
        continue
    total = np.prod(fact)
    print(total)
    if total > 500:
        print(n)
# print(n)