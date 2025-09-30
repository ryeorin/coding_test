def solution(picture, k):
    answer = []
    for i in picture:
        r=''
        for j in i:
            r+=j*k
        for _ in range(k):
            answer.append(r)
    return answer