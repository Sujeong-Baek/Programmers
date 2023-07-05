# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
def solution(board):

    N = len(board)
    directions = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0)}
    
    que = deque([(0,0,'d',0)])
    min_cost = [[float('inf')] * N for _ in range(N)]
    min_cost[0][0] = 0
       
    while que:
        r, c, d, cost = que.popleft()
        
        for direction, (dr, dc) in directions.items():            
            nr = r + dr
            nc = c + dc
            
            if 0<= nr < N and 0<= nc < N and board[nr][nc] == 0:     
        
                if d != direction:
                    current_cost = cost + 600
                elif d == direction:
                    current_cost = cost + 100  
                
                if min_cost[nr][nc] >= current_cost:                     
                    que.append((nr, nc, direction, current_cost))
                    min_cost[nr][nc] = current_cost
                   
    return min_cost[-1][-1] - 500