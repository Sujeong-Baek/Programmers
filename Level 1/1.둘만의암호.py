# https://school.programmers.co.kr/learn/courses/30/lessons/155652
def solution(s, skip, index):
    answer=''
    for el in s:        
        count=index        
        while count>0:          
            if el=='z':                
                el='a'
            else:   
                el=chr(ord(el)+1)    
            if el in skip:
                continue
            count-=1
        answer+= el
    return answer