# https://school.programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    answer = 0
    current = 0 # current번을 이제 확인해야함
      
    for station in stations:
        while current < station-w-1:
            answer += 1
            current += 1 + 2*w
        current = station+w

    while current < n:
            answer += 1
            current += 1 + 2*w      
            
    return answer

# 기지국과 연결되는 가장 끝부분을 저장해두고 갱신

#   #   #   #     #    #   >> 3
# 1,2,3,4,5,6,7,8,9,10,11

# 11	[4, 6]	1	3
# 0 >> 3 >> 5 >>  8 >> 11
