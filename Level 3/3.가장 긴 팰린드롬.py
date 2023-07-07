# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    answer = 0
    N = len(s)
    
    for i in range(N-1):
        for j in range(i+1,N,1):
            if check_palindrome(s[i:j+1]) and answer < j+1-i:
                answer = j+1-i                
    return 1 if answer == 0 else answer

def check_palindrome(s):
    N = len(s)
    for i in range(N//2): 
        if s[i] != s[N-i-1]:
            return False         
            
    return True