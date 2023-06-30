# https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    answer1 = [0] * len(sticker)
    answer1[0] = sticker[0]
    answer1[1] = sticker[0]
    for i in range(2, len(sticker)-1):
        answer1[i] = max(answer1[i-1], answer1[i-2] + sticker[i])
    
    answer2 = [0] * len(sticker)
    answer2[1] = sticker[1]
    for i in range(2, len(sticker)):
        answer2[i] = max(answer2[i-1], answer2[i-2] + sticker[i])
    
    return max(max(answer1), max(answer2))

