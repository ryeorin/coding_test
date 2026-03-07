def solution(n):
    answer = 0
    a=[]
    for i in range(1,1000):
        if i%3!=0 and '3' not in str(i):
            a.append(i)
    return a[n-1]