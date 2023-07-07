# https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    mini = 0
    maxi = min(times) * n
    
    while mini < maxi:
        mid = (mini+maxi)//2
        total = sum([mid//time for time in times]) 
        
        if total < n:
            mini = mid+1
        else:
            maxi = mid  
            
    return maxi