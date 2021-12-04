f = open('input.txt', 'r')
lines = f.readlines()

arr = []
values = []
singleMat = []
singleSum = 0
matrix_sums = []

remember_mat = []
remember_sum = 0
for line in lines:
    line = line.strip('\n')
    if len(line)>20:
        values = line.split(',')
    elif(line!=''):
        temp = []
        temp = line.split(' ')
        newA = []
        for x in temp:
            x.strip(' ')
            if x != '':
                newA.append(int(x))
                singleSum += int(x)
        singleMat.append(newA)
        remember_mat = singleMat
        remember_sum = singleSum
    else:
        arr.append(singleMat)
        matrix_sums.append(singleSum)
        singleMat = []
        singleSum = 0

arr.append(remember_mat)
matrix_sums.append(remember_sum)

arr.remove([])
matrix_sums.remove(0)
values_num = [int(numeric_string) for numeric_string in values]

def check_single_arr(ar):
    for x in ar:
        if x != -1:
            return False
    return True


def if_win(matrix):
    columns = [0, 0, 0, 0, 0]
    # check rows
    for array in matrix:
        if check_single_arr(array) == True:
            return True
    # check columns
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            columns[i] += matrix[j][i]

    for x in columns:
        if x==-5:
            return True
    return False

win_boards = []
called_num = -1
for num in values_num:
    # loop through matrixes

    for j in range(len(arr)):
        # check if board was already a winner
        if j in win_boards:
            continue
        # loop through arrays in matrix
        for h in range(len(arr[j])):
            # loop through numbers in array
            for i in range(len(arr[j][h])):
                if arr[j][h][i] == num:
                    # decrese sum of matrix
                    matrix_sums[j] = matrix_sums[j] - arr[j][h][i]
                    arr[j][h][i] = -1
        # check if win
        if if_win(arr[j]) == True:
            print(matrix_sums[j]*num)
            win_boards.append(j)
            continue
