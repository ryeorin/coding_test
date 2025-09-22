def solution(arr, query):
    c=0
    for q in query:
        if c%2==0:
            arr=arr[:q+1]
        else:
            arr=arr[q:]
        c+=1
    return arr