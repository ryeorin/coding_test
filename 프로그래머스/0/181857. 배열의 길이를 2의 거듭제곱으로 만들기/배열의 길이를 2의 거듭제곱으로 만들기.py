def solution(arr):
    for i in range(len(arr)):
        # 현재 길이가 2의 거듭제곱이면 그대로 반환
        if len(arr)==2**i:
            return arr
        # 현재 길이보다 큰데 가장 작은 2의 거듭제곱 
        elif len(arr)<2**i:
            arr+=[0]*((2**i)-len(arr))
            return arr