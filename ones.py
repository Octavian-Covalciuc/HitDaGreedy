lst = [0,1,0,1,1,0,1,1,0,1,1]
count = 0

for i in lst:   
    if count%2==0:
        i = i
    else:
        if (i == 1):
            i = 0
        else:
            i = 1
    if i == 1:
        continue
    else:
        i = 1
        count+=1

print(count)
