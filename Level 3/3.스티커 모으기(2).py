# https://school.programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    answer1 = 0
    answer2 = 0
    
    if len(sticker)%2 !=0:
        for idx, s in enumerate(sticker[1:],1):
            if idx%2 == 0 and idx != len(sticker)-1:
                answer1+=s

            elif idx%2 != 0 and idx != len(sticker)-1:
                answer2+=s
                
        answer1+=max(sticker[0],sticker[-1])
        
    else:
        for idx, s in enumerate(sticker):
            if idx%2 == 0:
                answer1+=s

            elif idx%2 != 0:
                answer2+=s
    return max(answer1, answer2)

