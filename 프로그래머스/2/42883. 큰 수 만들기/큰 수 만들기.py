def solution(number, k):
    stack = []
    # k개의 수를 지울건데 number에서 만들수있는 수들 중 가장 큰수
    # 지워서 숫자를 어떻게 만들지?
    for num in number:
        while stack and stack[-1]<num and k>0:
            stack.pop()
            k-=1
        stack.append(num)
    if k>0:
        stack=stack[:-k]
    
    return ''.join(list(map(str,stack)))