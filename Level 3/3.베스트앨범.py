# https://school.programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict
def solution(genres, plays):
    answer=[]
    genre2play=defaultdict(list)
    genre2total=defaultdict(int)

    for idx, (genre, play) in enumerate(zip(genres,plays)):
        genre2play[genre].append([-play, idx])
        genre2total[genre]+=play


    for genre, _ in sorted(genre2total.items(), key=lambda x: x[1], reverse=True):
        genre2play[genre].sort()
        answer.append(genre2play[genre][0][1])
        if len(genre2play[genre])>1:
            answer.append(genre2play[genre][1][1])  
            
    return answer
