f = open('input.txt', 'r')
lines = f.readlines()
arr = []

horizontal = 0
depth = 0
aim=0

for line in lines:
    chunks = line.split(' ')
    if chunks[0] == 'forward':
        depth = depth + ( int(chunks[1]) * aim )
        horizontal = horizontal + int(chunks[1])
    elif chunks[0] == 'up':
        aim  -= int(chunks[1])
    elif  chunks[0] == 'down':
        aim += int(chunks[1])


print(depth*horizontal)

5+40-2+8