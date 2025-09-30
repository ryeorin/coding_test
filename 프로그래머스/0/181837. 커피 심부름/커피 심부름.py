def solution(order):
    answer = 0
    for o in order:
        if o in ("hotamericano","americano","americanohot","iceamericano","americanoice","anything"):
            answer+=4500
        elif o in ("icecafelatte","cafelatteice","hotcafelatte","cafelattehot","cafelatte"):
            answer+=5000
    return answer