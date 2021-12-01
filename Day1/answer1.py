f = open('input.txt', 'r')
lines = f.readlines()

arr = []
count = 0

for line in lines:
    arr.append(int(line))

iter = 1
for x in arr[1:]:
    if x>arr[iter-1]:
        count+=1
    iter+=1

print(count)