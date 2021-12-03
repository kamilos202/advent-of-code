f = open('input.txt', 'r')
lines = f.readlines()
arr = []

gamma = ""
epsilon = ""

arr = []
for line in lines:
    arr.append(line)

count_arr=[]
for i in range(len(arr[0])-1):
    count_arr.append(0)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == '1':
            count_arr[j] = count_arr[j]+1

for x in count_arr:
    if x>=len(arr):
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'

print(int(gamma,2)*int(epsilon,2))