# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict
def solution(gems):

    gem_types=len(set(gems))
    current_gems2count=defaultdict(int)
    start=0
    end=0
    
    while end<len(gems):
        current_gems2count[gems[end]]+=1
        end+=1 
        
        if len(current_gems2count)==gem_types:
            while start<end:
                if current_gems2count[gems[start]]>1:
                    current_gems2count[gems[start]]-=1
                    start+=1
                else:
                    break
                    
            break
    
    return [start+1, end]