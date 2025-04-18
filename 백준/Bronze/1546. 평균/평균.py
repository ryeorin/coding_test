N =input()
score=list(map(int,input().split()))

M=max(score)
sum=sum(score)

print(sum*100/M/int(N))