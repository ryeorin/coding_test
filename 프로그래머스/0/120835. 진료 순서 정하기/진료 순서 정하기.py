def solution(emergency):
    answer = []
    em=sorted(emergency,reverse=True)
    
    for i in emergency:
        answer.append(em.index(i)+1)
    
    return answer