# 한 줄에 n개 만큼 입력 받고
# 소수인지 판별하고
# a+=1해서 개수 출력
n=int(input())
a=0
k=list(map(int,input().split()))
for x in k:
    for i in range(2,x+1):
        if x%i==0:
            if x==i:
                a+=1
            break
print(a)
    
    
    