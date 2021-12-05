f = open('input.txt', 'r')
lines = f.readlines()
arr = []

for line in lines:
    temp_ar = []
    split_ar = line.split(',')
    for x in split_ar:
        try:
            temp_ar.append(int(x))
        except:
            split = x.split(' -> ')
            temp_ar.append(int(split[0]))
            temp_ar.append(int(split[1]))

    arr.append(temp_ar)

j=-1
i=-1
for x in arr:
    if x[0]>j:
        j=x[0]
    if x[2]>j:
        j=x[2]
    if x[1] > i:
        i = x[1]
    if x[3] > i:
        i = x[3]

diag = []
for a in range(i+1):
    temp = []
    for b in range(j+1):
        temp.append(0)
    diag.append(temp)



for x in arr:
    if x[0] == x[2]:
        for a in range(min(x[1],x[3]),max(x[1],x[3])+1):
            diag[a][x[0]] += 1
    elif x[1] == x[3]:
        for b in range(min(x[0], x[2]), max(x[0], x[2]) + 1):
            diag[x[1]][b] += 1
    # Consider diagonal
    elif abs(x[0]-x[2]) == abs(x[1]-x[3]):
        # check direction
        if x[0]<x[2] and x[1]<x[3]:
            for c in range(abs(x[1]-x[3])+1):
                diag[x[1]+c][x[0]+c] += 1
        elif x[0]>x[2] and x[1]>x[3]:
            for c in range(abs(x[1]-x[3])+1):
                diag[x[3]+c][x[2]+c] += 1
        # check diagonal
        elif x[0]<x[2] and x[1]>x[3]:
            for c in range(abs(x[1] - x[3]) + 1):
                diag[x[3] + c][x[2] - c] += 1
        elif x[0]>x[2] and x[1]<x[3]:
            for c in range(abs(x[1] - x[3]) + 1):
                diag[x[1] + c][x[0] - c] += 1



for x in diag:
    print(x)

count=0
for x in diag:
    for num in x:
        if num >= 2:
            count+=1

print("Result:")
print(count)
