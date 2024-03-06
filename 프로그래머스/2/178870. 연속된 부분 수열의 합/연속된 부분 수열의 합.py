def solution(sequence, k):
    answer = []
    result = []
    start, end = 0, 0
    sum_s = sequence[start]
    sequence.append(0)
    while 1:
        if end >= len(sequence)-1: # 종료조건
            break
        if sum_s < k: # 만약 합이 k보다 작으면 end를 한칸 더 가야 함
            end += 1
            sum_s += sequence[end]
        elif sum_s == k: # 만약 합이 k와 같다면 result에 값을 저장하고, end한칸 start 한칸 
            result.append([start, end])
            end += 1
            sum_s += sequence[end]
            sum_s -= sequence[start]
            start += 1
        elif sum_s > k: # 만약 합이 k보다 크다면 start를 한칸 앞으로
            sum_s -= sequence[start]
            start += 1
        
        
        
    result.sort(key = lambda x: (x[1] - x[0], x[0]))    
    return result[0]