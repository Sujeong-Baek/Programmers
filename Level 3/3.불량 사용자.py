# https://school.programmers.co.kr/learn/courses/30/lessons/64064
def solution(user_id, banned_id):
    answer = 0
    banned_ids=[[] for _ in range(len(banned_id))]

    for idx, ban in enumerate(banned_id):        
        for num, user in enumerate(user_id):
            if len(ban)==len(user) and all(b=='*' or b==u for b, u in zip(ban, user)):
                banned_ids[idx].append(num)

    return answer
