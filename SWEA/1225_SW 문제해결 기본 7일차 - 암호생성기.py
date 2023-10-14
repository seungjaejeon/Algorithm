from collections import deque
T = 10
for _ in range(10):
    test_case = int(input())
    nums = deque(map(int,input().split()))
    cnt = 1
    while 1:
        num = nums.popleft() # 가장 왼쪽 숫자 pop
        num-= cnt # cnt만큼 감소
        cnt+=1 # cnt 1증가
        if cnt==6: # cnt가 6이 됐다면 다시 1로 바꾸어 1사이클 종료
            cnt = 1
        if num<=0: # 0이하라면 0을 추가하고 반복문 종료
            nums.append(0)
            break
        nums.append(num) # 그게 아니라면 감소한 num 다시 nums에 append
    print(f'#{test_case}', end=" ")
    for i in range(8):
        print(f'{nums[i]}', end=' ')
    print()
        