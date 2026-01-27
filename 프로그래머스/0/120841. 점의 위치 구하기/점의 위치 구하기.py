def solution(dot):
    answer = 0
    i,j=dot
    if i > 0 and j >0:
        answer+=1
    elif i <0 and j<0:
        answer+=3
    elif i<0 and j>0:
        answer+=2
    else:
        answer+=4
    return answer