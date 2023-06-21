# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)]) 
    while queue:
        current_word, current_count= queue.popleft()
        if current_word == target:
            return current_count
        
        for word in words:
            if len([c1 for c1,c2 in zip(current_word, word) if c1 != c2]) == 1:
                words.remove(word)
                queue.append((word, current_count+1))
    return 0