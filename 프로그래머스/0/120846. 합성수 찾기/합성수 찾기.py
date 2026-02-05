def solution(n):
    answer = 0
    # 자기 자신과 1뿐인 수 소수 2,3,5,7,11,13,17...
    # 1은 빼고
    for i in range(4,n+1):
        for j in range(2,i):
            if i%j==0:
                answer+=1
                break
    return answer