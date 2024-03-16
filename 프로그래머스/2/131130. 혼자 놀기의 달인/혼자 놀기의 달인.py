from collections import deque
def solution(cards):
    answer = 0
    cards = deque(cards)
    cards.appendleft(0)
    # n이하의 카드들
    # 1~n까지 상자들
    # 상자열고 숫자 확인하고 그 숫자에 해당하는 번호를 가진 상자를 열어감
    # 열려있는 상자를 만나면 종료
    # 이게 1번 그룹
    def choice(i):
        stack = []
        stack.append(i)
        cnt = 0
        while stack:
            box = stack.pop() # 깔 상자번호
            cnt += 1
            visited[box] = True
            next_box = cards[box] # 다음에 깔 상자 번호
            if visited[next_box] == False:
                stack.append(next_box)
            else:
                return cnt
    N = len(cards)
    visited = [False for i in range(N)]
    result = []
    for i in range(1, N):
        if visited[i] == False:
            res = choice(i)
            if res == N-1:
                return 0
            result.append(res)
    
    result.sort()    
    return result[-1] * result[-2]