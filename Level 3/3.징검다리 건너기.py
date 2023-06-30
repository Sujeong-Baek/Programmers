# https://school.programmers.co.kr/learn/courses/30/lessons/64062#
def solution(stones, k):
    answer = 0
    go=True
    while go:
        for idx, stone in enumerate(stones):
            if stone > 0 :
                s = 0
                stones[idx]-=1
            else:
                s += 1
                if s == k:
                    go=False
                    break
        if not go:
            break
        answer+=1
    return answer