# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from itertools import product
def solution(user_id, banned_id):
    answer = set()
    banned_ids=[[] for _ in range(len(banned_id))]

    for idx, ban in enumerate(banned_id):        
        for num, user in enumerate(user_id):
            if len(ban)==len(user) and all(b=='*' or b==u for b, u in zip(ban, user)):
                banned_ids[idx].append(num)
                
    for ids in product(*banned_ids):
        ids=set(ids)
        if len(ids)== len(banned_ids):
            answer.add(tuple(sorted(ids)))


    return len(answer)