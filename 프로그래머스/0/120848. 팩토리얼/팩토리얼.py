def solution(n):
    answer = 1
    fac=1
    for i in range(1,11):
        fac *=i
        if fac<=n:
            answer=i
    return answer