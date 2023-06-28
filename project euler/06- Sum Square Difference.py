till = 100
sum = 0
squares = 0

for i in range (1,100+1):
    sum +=i
    squares += i**2
    
diff =  sum**2 - squares
print (diff)