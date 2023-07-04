import calendar

print(
    sum(
        1 
        for i in range(1901,2000+1) 
        for j in range(1,12+1) 
        if calendar.weekday(i,j,1) == 6
        )
    )