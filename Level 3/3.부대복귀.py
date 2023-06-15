# https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import deque, defaultdict
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)    

    for source in sources:
        answer.append(bfs(graph, n, source, destination))
        
    return answer

def bfs(graph, n, source, destination):
    invited = [-1]*(n+1)
    invited[source] = 0
    queue = deque([source])
    
    while queue:
        node = queue.popleft()

        if node == destination:
            break
        
        for neighbor in graph[node]:
            if invited[neighbor] == -1:
                invited[neighbor] = invited[node] + 1
                queue.append(neighbor)
                
    return invited[destination]