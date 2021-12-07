f = open('input.txt', 'r')
line = f.readlines()

arr = [int(x) for x in line[0].split(',')]

# print(arr)

min_fuel = 0
for i in range(len(arr)):
    fuel = 0
    for j in range(len(arr)):
        fuel += abs(arr[i]-arr[j])
    if i == 0:
        min_fuel = fuel
    if fuel<min_fuel:
        min_fuel = fuel

print(min_fuel)