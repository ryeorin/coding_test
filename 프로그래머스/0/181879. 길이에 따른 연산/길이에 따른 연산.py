def solution(num_list):
    result =1
    for i in num_list:
        if len(num_list) >=11:
            return sum(num_list[::])
        else:
            result *=i
    return result
             