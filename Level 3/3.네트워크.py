# https://school.programmers.co.kr/learn/courses/30/lessons/43162
def solution(n, computers):
    answer=0
    visited=[0]*(n+1)
    graph=[[] for _ in range(n+1)]

    for i, computer in enumerate(computers,1):
        for j, node in enumerate(computer,1):
            if i != j and node==1:
                graph[i].append(j)

    
    for i in range(1, n+1):
        if visited[i]==0:
            answer+=1
            dfs(i, graph,  visited)

    return answer

def dfs(computer, graph,visited):
    visited[computer]=1
    for node in graph[computer]:
        if visited[node] == 0:
            dfs(node, graph, visited)