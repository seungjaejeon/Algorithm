def solution(name):
    answer = 0
    N = len(name)
    # 위 아래
    # 왼쪽 위
    def findcount(cur, ob):
        minus = ord(ob) - ord(cur)
        return min(minus, 26-minus) # 12
    
    def findlocation(cur, nxt):
        right = nxt-cur
        left = cur + (N-nxt-1)+1
        return min(left, right)
    
    loc = []
    
    for i, val in enumerate(name):
        answer += findcount('A', val)
        if val == 'A':
            loc.append(1)
        else:
            loc.append(0)
    count = 0
    max_count = 0
    endpoint = 0
    last_zero = 0
    first_zero = 21
    for i in range(len(loc)):
        if loc[i]==1:
            count += 1
        else:
            if first_zero == 21:
                first_zero = i
            last_zero = i
            count = 0 
            
        if count > max_count:
            endpoint = i+1
            max_count = count
    
    print(loc)
    print(endpoint-max_count-1 + 2*(N-endpoint))
    print(first_zero)
    if max_count == 0:
        location = N-1
    else:
        location = min(last_zero, 2*(endpoint-max_count-1) + N-endpoint, endpoint-max_count-1 + 2*(N-endpoint), N-first_zero)
    answer = location + answer
    if max_count == N:
        answer = 0
    # 가장 긴 길이 제거, 오왼
    # 오른쪽으로 쭉 -> N-1
    return answer