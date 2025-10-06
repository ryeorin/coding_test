import sys
input=sys.stdin.readline
output=[]

a=[True]*1000001
a[0]=a[1]=False

# 에라토스테네스의 체
for i in range(2, int(1000000**0.5)+1):
    if a[i]:
        for j in range(i*i, 1000001, i):
            a[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    
    for i in range(3, n//2+1,2):
        if a[i] and a[n-i]:
                output.append(f"{n} = {i} + {n - i}\n")
                break
    else:
        output.append("Goldbach's conjecture is wrong.\n")
        
sys.stdout.write(''.join(output))