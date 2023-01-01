# [           
# [1, 2, 3],
# [4, 5, 6], 
# [7, 8, 9]
# ]

# [
# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]
# ]

def transpose(arr):
    for row in range(len(arr)):
        for column in range(row, len(arr)):
            temp = arr[row][column]
            arr[row][column] = arr[column][row]
            arr[column][row] = temp
            print(arr)
    return arr

def mirror(arr):
    n = len(arr)
    for row in range(len(arr)):
        temp = arr[row][0]
        arr[row][0] = arr[row][n - 1]
        arr[row][n - 1] = temp
    return arr

def rotateMatrix(arr):
    transpose(arr)
    mirror(arr)
    return arr    

print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


