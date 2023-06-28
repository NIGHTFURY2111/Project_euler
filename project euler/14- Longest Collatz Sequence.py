# i'd get laid before this program finishes :(
import itertools as it
import time as tm
start = tm.perf_counter()

exclude = []
recorded = []
lists = {}
largest = 0
largest_num = 0

for j in range(10,1000001):
    i=j
    
    if i in lists:
        continue
    
    temp_list=[]
    create_list=[]
    in_List = False
    while i>1:
        temp_list.append(i)
    
        # i = (7/4)*i+(0.5)+(-1)**(i+1)*((5/4)*i+(0.5))
        if i%2 ==0:
            i = i/2
        else:
            i = (3*i)+1
            
        if i in lists:
            in_List = True
            break
        else:
            create_list.append(i)

    if in_List:
        length = len(temp_list)+lists[i]
    else:
        temp_list.append(1)
        length=len(temp_list)
    lists.update({j:length})
    
    for item in create_list:
        lists.update({item : len(temp_list[temp_list.index(item):])})
Key_max = max(lists, key = lists.get)  
print("The key with the maximum value is: ", Key_max)  

stop = tm.perf_counter()
print (f"time taken: {stop-start}")