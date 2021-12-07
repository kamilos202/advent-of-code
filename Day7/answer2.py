f = open('input.txt', 'r')
line = f.readlines()

arr = [int(x) for x in line[0].split(',')]

# print(arr)
def calculateSum(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res

max_pos = 0
min_pos = arr[0]
sum_of_all = 0
for x in arr:
    sum_of_all+=x
    if x<min_pos:
        min_pos=x
    if x>max_pos:
        max_pos=x



index = int(len(arr) / 2)
min_fuel = 10000000000000000
for i in range(min_pos, max_pos+1):
    fuel=0
    for j in range(len(arr)):
        fuel += calculateSum(abs(i-arr[j]))

    if fuel<min_fuel:
        min_fuel = fuel

print(min_fuel)
