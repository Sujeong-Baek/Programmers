# https://school.programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    N = len(triangle)
    dp = [[0]*i for i in range(1,N+1)]
    dp[-1] = triangle[-1]

    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j]=max(dp[i+1][j], dp[i+1][j+1])+triangle[i][j]
    return dp[0][0]