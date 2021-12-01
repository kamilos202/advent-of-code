f = open('input.txt', 'r')
lines = f.readlines()
arr = []

for line in lines:
    arr.append(int(line))

count = 0
iter = 3

sliding_sum = arr[0]+arr[1]+arr[2]
for x in arr[3:]:
    new_sliding_sum = sliding_sum-arr[iter-3]+x
    if new_sliding_sum > sliding_sum:
        count+=1
    sliding_sum = new_sliding_sum
    iter+=1

print(count)