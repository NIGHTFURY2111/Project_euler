import time
start = time.perf_counter()

def abundant_number_check(num):
    temp = [1]
    
    for j in range (2,int(num**0.5)+1):
        if j in temp:
            break
        x,y = divmod(num,j)
        if y ==0:
            temp.append(j)
            if x not in temp:
                temp.append(x)
    return sum(temp)

def isSum (num):
    for j in abundant_numbers:
        diff = num-j
        if diff in abundant_numbers:
            return False
    return True
        
        
abundant_numbers = set()
non_abundant_nums = [1]
till = 28123
for i in range(2,till+1):

    if abundant_number_check(i) > i:
        abundant_numbers.add(i)

    if isSum(i) :
        non_abundant_nums.append(i)

print(sum(non_abundant_nums))
stop = time.perf_counter()
print(stop - start)

