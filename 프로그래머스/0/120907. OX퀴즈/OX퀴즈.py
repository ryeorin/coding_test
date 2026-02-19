def solution(quiz):
    answer = []
    for i in quiz:
        i=i.split(" = ")
        if str(eval(i[0]))==str(i[1]):
            answer+="O"
        else:
            answer+="X"
    return answer