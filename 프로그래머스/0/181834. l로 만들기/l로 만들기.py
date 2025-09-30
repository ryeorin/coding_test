def solution(myString):
    for c in [chr(i) for i in range(ord('a'), ord('k')+1)]:
        myString = myString.replace(c, 'l')
    return myString