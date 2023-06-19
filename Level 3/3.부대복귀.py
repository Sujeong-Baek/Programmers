# https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import deque, defaultdict
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)    

    invited = [-1]*(n+1)
    invited[destination] = 0
    queue = deque([destination])
    
    while queue:
        node = queue.popleft()       

        for neighbor in graph[node]:
            if invited[neighbor] == -1:
                invited[neighbor] = invited[node] + 1
                queue.append(neighbor)
                
    return [invited[s] for s in sources]