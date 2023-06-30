# https://school.programmers.co.kr/learn/courses/30/lessons/64062#
def solution(stones, k):
    left = 0
    right = max(stones)

    while left < right:
        mid = (left+right) // 2
        zeros = [0 if stone <= mid else 1 for stone in stones]

        for idx, zero in enumerate(zeros):
            if zero == 0:
                i = idx
                while i < len(stones) and zeros[i] == 0:
                    i += 1
                if i - idx >= k:
                    right = mid
                    break
        else:
            left = mid + 1

    return right