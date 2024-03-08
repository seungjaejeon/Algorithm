def solution(elements):
    answer = 0
    N = len(elements)
    for i in range(N):
        elements.append(elements[i])
    # 중복값 제외 set
    # 수열 길이는 1부터 N까지 가능
    # 7 9 1 1 4 7 9 1 1 4
    result = []
    for i in range(1, N+1):
        start = 0
        end = start + i
        while 1:
            if end>2*N-1:
                break
            result.append(sum(elements[start:end]))
            start += 1
            end += 1
            
    answer = len(set(result))
    return answer