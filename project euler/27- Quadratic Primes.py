import itertools as it
import time



def nth_prime(length):
    global Prime_List
    Prime_List = [2,3]
    
    for i in it.count(Prime_List[-1],2):
        if i%3 ==0:
            continue
        
        Isprime= True
        limit = int(i ** 0.5)+1
        
        for j in Prime_List:
            if (i%j)==0:
                Isprime = False
                break
            
            if j > (limit):
                break
            
        if Isprime:
            Prime_List.append(i)
            if len(Prime_List) == length-2:
                break
    
    
def PrimeStringCheck(a,b):
    n=0
    while True:
        if (n**2 +a*n + b) not in Prime_List:
            if n <10:
                break
            else:
                allCombi[(a,b)] = n
                break
        n +=1
                
                
                
if __name__ =="__main__":
    start = time.perf_counter()
    n=4000
    nth_prime(n)
    Prime_List = set(Prime_List)
    global allCombi
    allCombi= {}
    for b in range(0,1000+1):
        for a in range(0,1000):
            
            PrimeStringCheck(a,b)
            PrimeStringCheck(a,-b)
            PrimeStringCheck(-a,b)
            PrimeStringCheck(-a,-b)

                    
                    
    print(max(allCombi, key = lambda x: allCombi[x])  )  
    print(max(allCombi.values())  )  



# Math - 11/12/2023 - 12:30
# English - 12/12/2023 - 12:30
# HTML5 - 13/12/2023 - 9:15