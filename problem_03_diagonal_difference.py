def diagonalDifference(arr):
    a = 0
    b = 0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][len(arr) - 1 - i]
    return abs(a - b)
