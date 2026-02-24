def solution(keyinput, board):
    # 시작 좌표
    x,y=0,0 
    
    # 이동 가능한 최대 범위 계산
    max_x=board[0]//2
    max_y=board[1]//2
    
    # keyinput을 하나씩 확인하면서 이동
    for key in keyinput:
        # 이동할 좌표를 일단 현재 좌표로 복사해놓고
        nx,ny=x,y
    
        # 방향키에 따라 다음 좌표를 계산
        if key=="left":
            nx-=1
        elif key=='right':
            nx+=1
        elif key=="down":
            ny-=1
        elif key =="up":
            ny+=1
        
        # 만약 다음 좌표가 범위 안이면 이동 확정
        if -max_x<=nx<=max_x and -max_y <=ny <=max_y:
            x,y=nx,ny
        # 범위 밖이면 아무 것도 안 함
        
    return [x,y]