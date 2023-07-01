# https://school.programmers.co.kr/learn/courses/30/lessons/43164
from collections import defaultdict
def soluton(tickets):
    answer = []
    depart2arrive = defaultdict(list)
    for depart, arrive in tickets:
        depart2arrive[depart].append(arrive)
    
    for depart in depart2arrive:
        depart2arrive[depart].sort(reverse=True)

    stack = ['ICN']
    while stack:
        top = stack[-1]
        
        if top not in depart2arrive or len(depart2arrive[top]) == 0:
            answer.append(stack.pop())
        
        else:
            stack.append(depart2arrive[top][-1])
            depart2arrive[top] = depart2arrive[top][:-1]

    return answer