largest = 0

for num in range(1,1000+1):
    is_repeating = False
    remainder_list = {}
    remainder = 1
    index = 0
    
    while True:
        index +=1
        if remainder in remainder_list:
            repeating_len = index - remainder_list[remainder]
            is_repeating = True
            break
        
        remainder_list[remainder] = index
        
        if remainder ==0:
            break
        
        elif remainder<num:
            remainder*=10
            continue
        
        else:
            remainder=remainder%num
            remainder*=10
            
    if is_repeating and repeating_len >largest:
        largest = num
    
print(largest)
