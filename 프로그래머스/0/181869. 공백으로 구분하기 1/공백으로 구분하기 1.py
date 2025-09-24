def solution(my_string):
    answer = []
    if ' ' in my_string:
        answer+=my_string.split()
    else:
        answer.append(my_string)
    return answer