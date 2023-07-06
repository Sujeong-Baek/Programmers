# https://school.programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
def solution(board):

    N = len(board)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    que = deque([(0,0,'d',0)])
    costs = [[[float('inf')]*4 for _ in range(N)] for _ in range(N)]
    costs[0][0] = [0,0,0,0]
       
    while que:
        r, c, d, cost = que.popleft()
        
        for direction, (dr, dc) in enumerate(directions):            
            nr = r + dr
            nc = c + dc
            
            if 0<= nr < N and 0<= nc < N and board[nr][nc] == 0:          
                current_cost = cost + 100 if d == direction else cost + 600
            
                if costs[nr][nc][direction]>current_cost:
                    costs[nr][nc][direction] = current_cost
                    que.append((nr, nc, direction, current_cost))

    return min(costs[-1][-1]) - 500