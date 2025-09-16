def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if not set(str(i))-set(['0','5']):
            answer.append(i)
        
    if len(answer)==0:
        answer.append(-1)
    return answer