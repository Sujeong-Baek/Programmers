# https://school.programmers.co.kr/learn/courses/30/lessons/72413
from collections import defaultdict, deque
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = defaultdict(list)
    for n1, n2, fee in fares:
        graph[n1].append([n2, fee])
        graph[n2].append([n1, fee])
    
    s2node = find_minfee_from_node_to_node(n, graph, s)
    a2node = find_minfee_from_node_to_node(n, graph, a)
    b2node = find_minfee_from_node_to_node(n, graph, b)

    for s, a, b in zip(s2node[1:], a2node[1:], b2node[1:]):
        total =  s + a + b
        if answer > total:
            answer = total

    return answer

def find_minfee_from_node_to_node(n, graph, start):
    que = deque(([start]))
    start2node = [float('inf')] * (n+1)
    start2node[start] = 0
    while que:
        node = que.popleft()
        
        for neighbor, fee in graph[node]:
            if start2node[neighbor] > start2node[node] + fee:
                start2node[neighbor] = start2node[node] + fee
                que.append(neighbor)
    return start2node