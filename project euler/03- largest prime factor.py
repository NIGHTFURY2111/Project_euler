def LargestPrimeFactor (number):
    '''return the largest Prime factor of a given number'''
    if number <1:
        return "enter a valid number"
    
    if number%2==0:
        number %= 2
        if number ==0:
            return  2
    for i in range (3,number+1,2):
        while number % i== 0:
            largest =  i
            number /= i
        if number<=1:
            return largest
        
        
GivenNumber = 600851475143

print(LargestPrimeFactor(GivenNumber))