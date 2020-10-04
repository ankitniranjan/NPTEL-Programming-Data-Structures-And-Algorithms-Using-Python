def contracting(l):
    prev = abs(l[1] - l[0])
    i = 1
    while i < len(l)-1:
        if abs(l[i] - l[i+1]) < prev:
            i += 1
        else:
            break
    if i == len(l) - 1:
        return True
    return False

def counthv(l):
    hill, valley = 0, 0
    for i in range(1, len(l)-1):
        if l[i] < l[i-1] and l[i] < l[i+1]:
            hill += 1
        elif l[i] > l[i-1] and l[i] > l[i+1]:
            valley += 1
    return [valley, hill]


def leftrotate(arr):
    n = len(arr)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = arr[i][j]
            arr[i][j] = arr[j][n-i-1]
            arr[j][n-i-1] = arr[n-i-1][n-j-1]
            arr[n-i-1][n-j-1] = arr[n-j-1][i]
            arr[n-j-1][i] = temp
    return arr
