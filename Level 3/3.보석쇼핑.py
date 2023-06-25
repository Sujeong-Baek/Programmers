# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict


def solution(gems):

    gem_types = len(set(gems))
    current_gems2count = defaultdict(int)
    start = 0
    end = 0
    leng = float('inf')
    answer = []
    while end < len(gems):
        current_gems2count[gems[end]] += 1
        while len(current_gems2count) == gem_types and start <= end:
            if leng > end - start: 
                leng = end - start  # 2
                answer = [start+1, end+1]
            current_gems2count[gems[start]] -= 1
            start += 1
        end += 1
    return answer

    # 1   2      3     4    5     6     7    8    9
print(solution(["AA", "AA", "AB", "AA", "AA", "AC", "AA", "AB", "AC"]))
print(solution(["AA", "AB", "AC"]))
