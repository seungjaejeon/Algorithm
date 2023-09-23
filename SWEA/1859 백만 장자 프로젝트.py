# DFS -> 시간초과 2^1000000
# greedy
# 이득의 최대
# 가장 큰 수를 찾고 그 전까지의 가격들을 모두 구매하고 큰수에서 모두 판매 -> 배열의 끝까지
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    price= list(map(int , input().split()))
    result = 0
    while len(price) != 0:
        max_price = max(price)
        now = price.index(max_price)

        buy = price[:now]
        price = price[now+1:]
        for purchase in buy:
            result += abs(purchase - max_price)
    print(f"#{test_case} {result}")