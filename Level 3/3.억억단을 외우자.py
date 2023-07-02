# https://school.programmers.co.kr/learn/courses/30/lessons/138475
from collections import defaultdict
def solution(e, starts):
    num2count=defaultdict(int)
    for num in range(1,e+1):
        for i in range(num, e+1, num):            
            num2count[i] += 1

    num2min_num=defaultdict(int)
    for num in range(e, min(starts)-1, -1):        
        if max_count<=num2count[num]:
            max_count=num2count[num]
            min_num=num
        num2min_num[num] = min_num
                        
    return [num2min_num[start] for start in starts]

# 6: 4 - [1,2,3,6]
# 6 % 6 == 0
# 6 % 5 != 0
# ...
# n번

# 1 * 6 == 6, + 1

# 2 * 1 == 2, num2count[2] += 1
# 2 * 2 == 4, num2count[4] += 1
# 2 * 3 == 6, num2count[6] += 1
# 2 * 4 == 8, num2count[8] += 1

# 3 * 2 == 6, + 1
# 6 * 1 == 6, + 1