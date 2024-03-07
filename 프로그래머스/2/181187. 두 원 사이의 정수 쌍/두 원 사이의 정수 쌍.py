import math
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        b2 = r2**2 - i**2
        j = int(math.sqrt(b2))
        answer += j + 1
        b1 = r1**2 - i**2
        if i < r1:
            k = math.sqrt(b1)
            if k == int(k):
                answer -= k
            else:
                k = int(k)
                answer -= k + 1
    answer *= 4
    return answer