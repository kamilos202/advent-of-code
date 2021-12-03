f = open('input.txt', 'r')
lines = f.readlines()

arr = []
for line in lines:
    new_a = [ch for ch in line]
    new_a = new_a[:-1]
    arr.append(new_a)


def one_times(arr):
    count_arr = []
    for i in range(len(arr[0])):
        count_arr.append(0)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '1':
                count_arr[j] = count_arr[j] + 1
    return count_arr

def keep_one(i,ar):
    new_array = []
    for j in range(len(ar)):
        if ar[j][i] == '1':
            new_array.append(ar[j])
    return new_array

def keep_zero(i,ar):
    new_array = []
    for j in range(len(ar)):
        if ar[j][i] == '0':
            new_array.append(ar[j])
    return new_array



test=[
['0','0','1','0','0'],
['1','1','1','1','0'],
['1','0','1','1','0'],
['1','0','1','1','1'],
['1','0','1','0','1'],
['0','1','1','1','1'],
['0','0','1','1','1'],
['1','1','1','0','0'],
['1','0','0','0','0'],
['1','1','0','0','1'],
['0','0','0','1','0'],
['0','1','0','1','0']]



# compute oxygen generator rating
most_arr = arr
iter = 0
while len(most_arr) != 1:
    count = one_times(most_arr)
    #print(len(most_arr))
    # print(most_arr)
    # print(count)
    # print(iter)
    #print(count[iter])
    if count[iter]>=len(most_arr)/2:
        most_arr = keep_one(iter, most_arr)
    else:
        most_arr = keep_zero(iter, most_arr)
    iter+=1

print(most_arr)

# compute CO2 scrubber rating
least_arr = arr
iter = 0
while len(least_arr) != 1:
    count = one_times(least_arr)
    # print(len(least_arr))
    # print(least_arr)

    if count[iter]<len(least_arr)/2:
        least_arr = keep_one(iter, least_arr)
    else:
        least_arr = keep_zero(iter, least_arr)
    iter+=1

oxygen=""
co2=""
for i in range(len(least_arr[0])):
    oxygen+=most_arr[0][i]
    co2+=least_arr[0][i]

print(int(oxygen,2))
print(int(co2,2))
print("Result:")
print(int(oxygen,2)*int(co2,2))
