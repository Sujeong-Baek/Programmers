# https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)    
        
    for source in sources:
        answer.append(bfs(graph, source, destination))
    return answer

def bfs(graph, source, destination):
    pass