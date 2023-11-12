T = int(input())
for _ in range(1, T + 1):
    test_case = int(input())
    N = 1000
    score = dict()
    score_list = list(map(int, input().split()))
    for i in range(N):
        if score_list[i] in score.keys():
            score[score_list[i]]+=1
        else:
            score[score_list[i]] = 1
    max_count = 0
    max_count_score = 0
    for i in range(101):
        if i in score.keys():
            if max_count <= score[i]:
                max_count_score = i
                max_count = score[i]
    
    print(f'#{test_case} {max_count_score}')