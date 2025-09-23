def solution(num_list):
    count =0
    for idx,i in enumerate(num_list):
        while i >1:
            if i%2==0:
                i//=2 # i=i//2 정수 나누기
            else:
                i=(i-1)//2
            count+=1
        num_list[idx]=i
    return count