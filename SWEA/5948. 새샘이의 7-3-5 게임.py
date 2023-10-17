from itertools import combinations
T = int(input())
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    result = []
    for i in combinations(range(7), 3):
        result.append(nums[i[0]]+nums[i[1]]+nums[i[2]])
    result_set = list(set(result))
    result_set.sort(reverse=True)
    print(f'#{test_case} {result_set[4]}')