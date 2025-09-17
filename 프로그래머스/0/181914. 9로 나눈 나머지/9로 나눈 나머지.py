def solution(number):
    answer = 0
    a=list(map(int,number))
    answer=sum(a)%9
    
    
    return answer