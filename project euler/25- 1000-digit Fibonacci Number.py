lst = []
first, second = 0,1
while True:
    lst.append(first)
    if len(str(first))==1000:
        print(lst.index(first))
        break
    first, second = second, first + second