def SumOfMultipleOf3And5 (FirstNDigits):
    '''returns the sum of all the multiples of 3 and 5 between 0 and FirstNDigits '''
    sum=0
    for cycle in range (FirstNDigits):
        if cycle%3 ==0:
            sum += cycle
            continue
        elif cycle %5 ==0:
            sum += cycle
            continue
    return sum

N = 1000
print(SumOfMultipleOf3And5(N))
        