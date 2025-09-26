def solution(arr, flag):
    answer = []
    for i in range(0,len(flag)):
        if flag[i]:
            answer.extend([arr[i]]*arr[i]*2)
        else :
            answer=answer[:-arr[i]]
    return answer