def solution(answers):
    answer = []
    count1=0
    count2=0
    count3=0
    # 1번 수포자가 찍는 방식
    m1=[1,2,3,4,5]
    # 2번 수포자가 찍는 방식
    m2=[2,1,2,3,2,4,2,5]
    # 3번 수포자 찍는 방식
    m3=[3,3,1,1,2,2,4,4,5,5]
    
    # answers 값이랑 찍는 거랑 비교했을 때
    for i in range(len(answers)):
        if (m1[i-len(m1)*(i//len(m1))]==answers[i]):
            count1+=1
        if (m2[i-len(m2)*(i//len(m2))]==answers[i]):
            count2+=1
        if (m3[i-len(m3)*(i//len(m3))]==answers[i]):
            count3+=1
            
    if (count1==max(count1,count2,count3)):
        answer.append(1)
    if (count2==max(count1,count2,count3)):
        answer.append(2)
    if (count3==max(count1,count2,count3)):
        answer.append(3)
        
    return answer