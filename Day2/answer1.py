f = open('input.txt', 'r')
lines = f.readlines()
arr = []

horizontal = 0
depth = 0
for line in lines:
    chunks = line.split(' ')
    if chunks[0] == 'forward':
        horizontal = horizontal + int(chunks[1])
    elif chunks[0] == 'up':
        depth = depth - int(chunks[1])
    elif  chunks[0] == 'down':
        depth = depth + int(chunks[1])

print(depth*horizontal)