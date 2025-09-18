def solution(my_string, is_suffix):
    for i in range(1,len(my_string)+1):
        a=my_string[-i:]
        if is_suffix == a:
            return 1
    else:
        return 0