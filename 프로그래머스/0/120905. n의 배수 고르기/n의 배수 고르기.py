def solution(n, numlist):
    answer = []
    for i in range(len(numlist)):
        for a in range(1,max(numlist)+1):
            if n*a == numlist[i]:
                answer.append(numlist[i])
                
    return answer