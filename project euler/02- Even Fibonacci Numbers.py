def SumOfEvenFibonacci (Upperbound):
    '''return the sum of all the even numbers in the fibonacci series up till Upperbound'''
    sum = 0
    [first,Second,Adder] = [0,1,0]
    
    while first < Upperbound:
        if first % 2 == 0:
            sum += first
        Adder = first + Second
        first = Second
        Second = Adder
    
    return sum


n= 4000000
print (SumOfEvenFibonacci(n))