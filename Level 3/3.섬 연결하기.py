# https://school.programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    parent = [node for node in range(n)] # parent[i]: node i의 parent                     # rank[i]: node i의 height
    costs.sort(key = lambda x:x[2])

    for n1, n2, cost in costs:
        if find_parent(n1, parent) != find_parent(n2, parent):
            node_union(n1, n2, parent)
            answer += cost
    return answer

# parent[1] = 3
# parent[3] = 3
# parent[5] = 3
# parent[7] = 7
# 1 -> 3 -> 5 -> 7, 
# find_parent(1,) = 7
# find_parent(3,) = 7
# find_parent(5,) = 3
# find_parent(7,) = 7
def find_parent(n, parent): 
    
    if parent[n] == n:
        return n
    for p in range(len(parent)):
        if parent[n] != p:
            return

def node_union(n1, n2, parent):
    root1 = find_parent(n1, parent)
    root2 = find_parent(n2, parent)
    parent[root1] = root2

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))

# recursive vs iterative

# fibonacci
# 1,1,2,3,4,7,11,..
def fib(i):
    if i <= 2:
        return 1
    return fib(i-1) + fib(i-2)

def fib2(i):
    if i <= 2:
        return 1
    a, b = 1,1
    for _ in range(i-2):
        a, b = b, a + b
    return b