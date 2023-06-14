# https://school.programmers.co.kr/learn/courses/30/lessons/138475
def solution(e, starts):
    answer = []
    num2count={}
    for num in range(1,e+1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        num2count[num]=count

    for start in starts:
        max_count=0
        min_num=0

        for num in range(e, start-1, -1):
            if max_count<=num2count[num]:
                max_count=num2count[num]
                min_num=num
        answer.append(min_num)
            
    return answer