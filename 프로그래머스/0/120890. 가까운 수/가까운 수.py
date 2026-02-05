def solution(array, n):
    array.sort()
    answer = []
    for i in array:
        answer.append(abs(i-n))
        
    return array[answer.index(min(answer))]