f = open('input.txt', 'r')
lines = f.readlines()

arr = []

arr = lines[0].split(',')
array = []
for x in arr:
    array.append(int(x))



for i in range(80):
    temp = []
    for j in range(len(array)):
        array[j] -= 1
        if array[j] == -1:
            array[j] = 6
            temp.append(8)
    array += temp

print(len(array))