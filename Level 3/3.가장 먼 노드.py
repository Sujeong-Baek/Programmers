# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import defaultdict, deque
def solution(n, edge):
    
    graph=defaultdict(list)

    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    que = deque(([1]))
    distances = [-1] * n+1
    distances[1] = 0

    while que:
        node = que.popleft()

        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                que.append(neighbor)

    far_node = max(distances)
    return distances.count(far_node)