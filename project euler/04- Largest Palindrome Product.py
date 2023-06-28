def PalindromeCheck (word):
    '''checks if a string is Palindrome'''
    palindrome = True
    
    for i in range (len(word)):
        if word[i] == word[-(i+1)]:
            continue    
        else:
            palindrome=False 
            break
    return palindrome


# first = 999
# second = 999
# while second>1:
    
#     while first>99:
#         IsPalindrome = PalindromeCheck(str(first*second))
#         print(f"{first*second}\n{first} {second}")
#         if IsPalindrome:
#             break
#         first-=1
        
#     if IsPalindrome:
#         break
#     second-=1
#     first = 999

store=[i*j 
    for i in range (100,1000)
    for j in range (100,1000)]

# for i in range (100,1000):
#     for j in range (100,1000):
#         store.append(i*j)
store.sort(reverse=True)
for num in store:
    if PalindromeCheck(str(num)):
        print(num)
        break
        