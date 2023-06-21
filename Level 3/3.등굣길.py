# https://school.programmers.co.kr/learn/courses/30/lessons/42898
from collections import deque
def solution(m, n, puddles):
    visited=[[0]*m for _ in range(n)]
    queue=deque([(0,0)])
    visited[0][0]=1

    while queue:
        r, c = queue.popleft()

        for dr, dc in [[1,0],[0,1]]:
            nr=r+dr
            nc=c+dc

            if 0<=nr<n and 0<=nc<m and [nr+1,nc+1] not in puddles:
                if visited[nr][nc] == 0:
                    queue.append((nr,nc))
                
                visited[nr][nc]+=visited[r][c]

    return visited[n-1][m-1] % 1000000007