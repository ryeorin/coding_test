from itertools import combinations
#nums에서 n수 만큼 짝 지어줄거야, 연결된걸 봤을때 겹치지 않는 수들 찾기,그것들의 개수
def solution(nums):
    n=len(nums)//2
    pairs=len(set(nums))
    return min(pairs,n)