f = open('test.txt', 'r')
lines = f.readlines()

# arr = []
#
# arr = lines[0].split(',')
# array = []
# for x in arr:
#     array.append(int(x))
#
#
#
# for i in range(256):
#     print(i)
#     temp = []
#     for j in range(len(array)):
#         array[j] -= 1
#         if array[j] == -1:
#             array[j] = 6
#             temp.append(8)
#     array += temp
#
# print(len(array))

file = open("input.txt", "r").read()

def solve(s, days = 256):
	res = [int(i) for i in s.split(",")]
	cnt = [0 for i in range(10)]

	for i in res:
		cnt[i] += 1

	for i in range(days):
		nv = [0 for i in range(10)]
		for j in range(1, len(cnt)):
			nv[j - 1] += cnt[j]
		nv[6] += cnt[0]
		nv[8] += cnt[0]
		cnt = nv

	return sum(cnt)

print(solve(file))