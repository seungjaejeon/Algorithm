from itertools import combinations
T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    result = []
    for i in combinations(range(7), 3): # 0부터 6까지중 3가지를 고르는 경우
        result.append(nums[i[0]]+nums[i[1]]+nums[i[2]]) # ex) i = (1,3,4)
    result_set = list(set(result)) # 중복제거
    result_set.sort(reverse=True) # 정렬
    print(f'#{test_case} {result_set[4]}') # 5번째