arr = [0,1,3,0,3]
j= []
count = 0
for i in arr:
    if i == 0:
        count +=1
    if i != 0:
        j.append(i)
for a in range(count):
    j.append(0)

print(j)