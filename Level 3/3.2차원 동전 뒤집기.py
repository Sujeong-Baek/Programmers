# https://school.programmers.co.kr/learn/courses/30/lessons/131703
def solution(beginning, target):
    answer = 0
    R=len(target)
    C=len(target[0])
    for r in range(R):
        if beginning[r][0] != target[r][0]:
            flip_coin(beginning, r, 'r')
            answer+=1
            
    for c in range(C):
        if beginning[0][c] != target[0][c]:
            flip_coin(beginning, c, 'c')
            answer+=1

    return answer if beginning == target else -1

def flip_coin(beginning, n, rc):
    if rc=='r':
        for idx, coin in enumerate(beginning[n]):
            if coin == 0:
                beginning[n][idx] = 1
            else:
                beginning[n][idx] = 0
    else:
        for r, coins in enumerate(beginning):
            for c, coin in enumerate(coins):
                if c == n and coin == 0:
                    beginning[r][n] = 1
                elif c==n and coin == 1:
                    beginning[r][n] = 0
                
            