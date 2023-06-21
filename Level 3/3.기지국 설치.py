# https://school.programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    answer=0
    apart=[0]*(n+1)

    for station in stations:
        start=max(station-w, 1)
        end=min(station+w, n+1)
        apart[start:end+1]=[1]*(end-start+1)

    start=1
    while start<=n:
        if apart[start]==0:
            end=min(start+2*w+1, n+1)
            apart[start:end]=[1]*(end-start)
            answer+=1

    return answer