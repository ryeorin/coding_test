def solution(arr1, arr2):
    if len(arr1)==len(arr2):
        # arr1의 원소의 합이랑 arr2 원소의 합 비교해서 더 큰쪽이 크고 같으면 같다.
        # 거기서 arr1 더 크면 1, arr2가 더 크면 -1, 같으면 0
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1)<sum(arr2):
            return -1
        elif sum(arr1)==sum(arr2):
            return 0
    else:
        if len(arr1)>len(arr2):
            return 1
        elif len(arr1)<len(arr2):
            return -1
        elif len(arr1)==len(arr2):
            return 0