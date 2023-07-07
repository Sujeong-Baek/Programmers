# https://school.programmers.co.kr/learn/courses/30/lessons/42627
from collections import defaultdict
def solution(jobs):
    jobs.sort()
    answer = jobs[0][1]
    current_time = jobs[0][0] + jobs[0][1]
    time2starts = defaultdict(list)

    for start, time in jobs[1:]:
        time2starts[time].append(start)

    time2starts = dict(sorted(time2starts.items(), key = lambda x:x[0]))

    completed_job = 1
    while completed_job < len(jobs):
        min_start = float('inf')
        check_work = False

        for time , starts in time2starts.items():
            if len(starts) > 0 and starts[0] <= current_time:
                answer += time + current_time - starts[0]
                current_time += time
                starts.pop(0)
                completed_job += 1
                check_work = True
                break
            elif len(starts) > 0 and starts[0] < min_start:
                min_start = starts[0]


        if check_work is False:
            current_time = min_start

    return answer // len(jobs)