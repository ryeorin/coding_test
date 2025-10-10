def solution(n, lost, reserve):
    # 여벌있는 학생들 reserve +- 1해서 번호를 정해서
    # 그 번호가 잃어버린 사람들의 번호랑 같으면 answer+1
    # reserve 숫자만큼 answer에 담아주고
    # 안 잃어버린 학생들 수
    # 이걸 탐욕적으로 접근하려면 바로 앞번호, 바로 뒷번호 학생들에게 빌려주는게
    # 정당성 : 빌려줄 대상이 끝이나면 수업 들을수있는 학생수를 합한다.
    # 1부터 n+1에서 reserve에 있거나 lost에 없는 학생 수 만큼 answer에 추가해
    lost.sort()
    reserve.sort()
    
    for k in reserve[:]:
        if k in lost:
            reserve.remove(k)
            lost.remove(k)
            
    for i in reserve:
        a=i+1
        b=i-1
        if b in lost:
            lost.remove(b)

        elif a in lost:
            lost.remove(a)
            
    return n-len(lost)