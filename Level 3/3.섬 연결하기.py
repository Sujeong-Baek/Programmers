# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    parent = [node for node in range(n)]
    rank = [0] * n
    costs.sort(key = lambda x:x[2])

    for n1, n2, cost in costs:
        if find_parent(n1, parent) != find_parent(n2, parent):
            node_union(n1, n2, parent, rank)
            answer += cost
    return answer

def find_parent(n, parent):
    if parent[n] != n:
        parent[n] = find_parent(parent[n], parent)
    return parent[n]

def node_union(n1, n2, parent, rank):
    root1 = find_parent(n1, parent)
    root2 = find_parent(n2, parent)

    if rank[root1] > rank[root2]:
        parent[root1] = root2
    else: 
        parent[root2] = root1
        if parent[root1] == parent[root2]:
            rank[root1] += 1