T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    week = list(map(int,input().split()))
    min_result = float('inf')
    for i, val in enumerate(week):
        if val == 1: # 1인경우 전부 해보기 -> 시작일자에 따라서 값이 바뀌기 때문에
            result = 0
            index = i # 현재의 인덱스 저장
            temp = N # 임시값 저장
            while temp:
                if week[index]==1: # 수업이 있으면
                    temp-=1 # 들어야 하는 수업 - 1
                index =  (index+1)%7 # 인덱스 1증가
                result += 1 # 카운트
            min_result = min(result, min_result) # 최소인 경우 저장
    print(f'#{test_case} {min_result}') # 출력