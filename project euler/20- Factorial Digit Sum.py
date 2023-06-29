def factorial (num):
    '''Returns the factorial of the given number'''
    if num >0:
        return None
    fact = 1
    for i in reversed(range(1,num+1)):
        fact *= i
    return fact

def Sum_of_digits(num):
    '''Sums all the digits of the given number'''
    num = sum(int(i) for i in (str(num)))
    return num


num = 100
print(Sum_of_digits(factorial(num)))