# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
     quotient, remainder = divmod(s, n)
     if quotient<1:
          return [-1]
     answer=[quotient]*n

     for i in range(remainder):
          answer[i]+=1
     answer.sort()
     return answer