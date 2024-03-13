def solution(picks, minerals):
    answer = 0
    # 곡갱이 1 = 5광물
    # 곡갱이 하나 시작하면 깨질때까지 사용해야함
    # 광물은 주어진 순서 => queue or stack
    # 종료 조건 => 모든 광물 캐기, 모든 곡갱이 사용
    
    # 최소한의 피로도를 return
    minerals.reverse()
    dp = [[0 for i in range(3)] for j in range(min(len(minerals)//5 + 1, sum(picks)))]
    def digging(start):
        i = 5
        while minerals and i > 0:
            mineral = minerals.pop()
            dp[start][0] += 1
            if mineral == "diamond":
                dp[start][1] += 5
                dp[start][2] += 25 # 돌로캐면
            elif mineral == "iron":
                dp[start][1] += 1 # 철로 캐면
                dp[start][2] += 5 # 돌로 캐면
            elif mineral == "stone":
                dp[start][1] += 1
                dp[start][2] += 1
            i -= 1
        return
    N = len(minerals)
    for i in range(sum(picks)):
        digging(i)
    # 광물 피로도 표
    # 가장 적은 피로도 루트를 구하면 됨
    # 돌부터 선택, 철 선택, 나머지 다이아
    dp.sort(key = lambda x: (-x[2],-x[1],-x[0]))
    start = 0
    for i in range(3):
        pick = picks[i]
        while pick > 0 and start < len(dp):
            answer += dp[start][i]
            start += 1
            pick -= 1
    
    return answer