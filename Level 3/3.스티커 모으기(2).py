# https://school.programmers.co.kr/learn/courses/30/lessons/12971
from collections import deque
def solution(sticker):
    answer = 0
    
    for idx in range(3):
        answer=max(answer, serch_sticker_score(idx, sticker)) 
    return answer

def serch_sticker_score(idx, sticker):
    answer = 0
    que=deque()

    visited = [0] * (len(sticker))
    visited[idx]=1
    visited[(idx+1)% len(sticker)]=1
    visited[(idx-1)% len(sticker)]=1
    
    que.append([idx, sticker[idx], visited])
    
    while que:      
        idx, score, visited = que.popleft()
        answer = max(answer,score)
      
        for jump in [2, 3]:
            current_idx = (idx + jump) % len(sticker)
            current_visited=[num for num in visited]
            
            if not current_visited[current_idx]:
                start=max(0,current_idx-1)
                end=min(current_idx+2,len(sticker))                
                current_visited[start:end]=[1]*(end-start)
                que.append([current_idx, score+sticker[current_idx],current_visited])
                
    return answer

