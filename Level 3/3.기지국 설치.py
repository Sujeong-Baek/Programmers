# https://school.programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    end = 0 # end번까지 확인함
    answer = 0
    for station in stations:
        while end < station-w-1:
            answer += 1
            end += 1 + 2*w
        end = station+w

    while end < n:
            answer += 1
            end += 1 + 2*w      
            
    return answer

# 숙제: current = 1로 짜보기

# 기지국과 연결되는 가장 끝부분을 저장해두고 갱신

#   #   #   #     #    #   >> 3
# 1,2,3,4,5,6,7,8,9,10,11

# 11	[4, 6]	1	3
# 0 >> 3 >> 5 >>  8 >> 11
