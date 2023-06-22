# https://school.programmers.co.kr/learn/courses/30/lessons/12987
def solution(A, B):
    A.sort()
    B.sort()
    answer=0
    for a in A:
        while B:
            if B[0]>a:
                B.pop(0)
                answer+=1
                break
            else:
                B.pop(0)
    return answer