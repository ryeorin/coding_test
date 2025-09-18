def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        a=intStrs[i]
        b=int(a[s:s+l])    
        if k < b:
            answer.append(b)
    return answer