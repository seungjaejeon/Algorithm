T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split()) # M초간 K개의 붕어빵
    client = list(map(int, input().split())) # 기다리는 시간 없이 제공한다면 possible
    client.sort()
    max_c = client[-1]
    dic = dict()
    for i in client:
        if i in dic:
            dic[i] += 1
        else: dic[i] = 1
    index = 0
    count = 0
    result = "Possible"
    for i in range(max_c+1): # 최대 초까지 1초씩 증가 시키면서
        if index>=N:
            break
        if i%M==0 and i != 0: # M초가 지날때마다
            count += K
        if client[index] == i:
            count -= dic[i]
            if count<0:
                result = 'Impossible'
                break
            index += 1
    print(f'#{test_case} {result}')