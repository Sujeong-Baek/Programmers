# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer=0
    routes.sort(key=lambda x:x[1])
    last_camera=-30001

    for start, end in routes:
        if last_camera<start:
            answer+=1
            last_camera=end

    return answer
