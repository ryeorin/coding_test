def solution(arr):
    idx = []
    for x, y in enumerate(arr):
        if y == 2:
            idx.append(x)
    if idx:
        return arr[idx[0]:idx[-1]+1]
    else:
        return [-1]