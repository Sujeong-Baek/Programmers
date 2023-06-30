# https://school.programmers.co.kr/learn/courses/30/lessons/64062#
def solution(stones, k):
    left = 0
    right = max(stones)
    count = 0
    while left < right:
        mid = (left+right) // 2
        zeros = [0 if stone <= mid else 1 for stone in stones ]

        for zero in zeros:
            if zero == 0:
                count+=1
                if count == k:
                    right = mid
                    break
            else:
                count = 0
        else:
            left = mid + 1
        
    return right