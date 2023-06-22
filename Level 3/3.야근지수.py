# https://school.programmers.co.kr/learn/courses/30/lessons/12927
from heapq import heapify,heappop,heappush
def solution(n, works):
    if sum(works)<=n:
        return 0
    
    works=[(-1)*work for work in works]
    heapify(works)

    while n>0:
        heappush(works, heappop(works)+1)
        n-=1
        
    return sum([work**2 for work in works])