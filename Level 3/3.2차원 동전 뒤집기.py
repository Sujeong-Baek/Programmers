# https://school.programmers.co.kr/learn/courses/30/lessons/131703
def solution(beginning, target):
    answer1 = 0
    R=len(target)
    C=len(target[0])
    beginning2  = [r[:] for r in beginning]
    answer2 =0
    
    for r in range(R):
        if beginning[r][0] != target[r][0]:
            flip_coin(beginning, r, 'r')
            answer1+=1
            
    for c in range(C):
        if beginning[0][c] != target[0][c]:
            flip_coin(beginning, c, 'c')
            answer1+=1

    for c in range(C):
        if beginning2[0][c] != target[0][c]:
            flip_coin(beginning2, c, 'c')
            answer2+=1
            
    for r in range(R):
        if beginning2[r][0] != target[r][0]:
            flip_coin(beginning2, r, 'r')
            answer2+=1          

    if beginning== target and beginning2 == target:
        return min(answer1, answer2)
    if beginning != target and beginning2 == target:
        return answer2
    if beginning == target and beginning2 != target:
        return answer1
    # if beginning != target and beginning2 != target:
    return -1
    
    # return answer if beginning == target else -1

# o x o x o
# x x o x x
# o o x o o

# o x x x o
# x x x x x
# o o o o o

# o x x x o
# x x x x x
# x x x x x

# o x o x o
# x x o x x
# x x o x x

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
                
            