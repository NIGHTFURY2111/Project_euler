num = 2
power = 80000
answer = list(str(num**power)[:])
sum = 0
for i in answer:
    sum +=int(i)
sum = str(sum)
print(sum)
finale = 0
while int(sum)>=10:
    for j in (sum):
        finale += int(j)
    sum = str(finale)
    finale = 0
print(sum)