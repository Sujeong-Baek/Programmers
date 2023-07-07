# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    answer = 0
    
    for idx in range(len(s)):
        length = find_len_pelindrome(idx, s)
        if answer < length:
            answer = length
    return answer

def find_len_pelindrome(idx, s):
    idxl_1 = idx
    idxr_1 = idx
    while idxl_1-1>=0 and idxr_1+1<len(s) and s[idxl_1-1] == s[idxr_1+1]:
        idxl_1 -= 1
        idxr_1 += 1
        
    answer1 = idxr_1 - idxl_1 + 1
        
    idxl_2 = idx+1
    idxr_2 = idx
    while idxl_2-1>=0 and idxr_2+1<len(s) and s[idxl_2-1] == s[idxr_2+1]:
        idxl_2 -= 1
        idxr_2 += 1
        
    answer2 = idxr_2 - idxl_2 + 1
    
    return max(answer1, answer2)