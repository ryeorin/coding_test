def solution(rank, attendance):
    answer = 0
    a=[]
    for i in range(len(attendance)):
        if attendance[i]:
            a.append(rank[i])
    a=sorted(a)
    return rank.index(a[0])*10000+rank.index(a[1])*100+rank.index(a[2])