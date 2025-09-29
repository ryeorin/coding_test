def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            print(i)
            answer+=i
    return answer