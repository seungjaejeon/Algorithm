W = int(input())
words = input().split()
# code below
dp = [0 for i in range(len(words))] # dp words의 개수만큼 리스트 생성
lenght = [len(i) for i in words] # words의 단어들의 길이를 저장하는 리스트
dp[0] = (W-lenght[0])**3 # dp[0]에 penalty를 넣음
for i in range(1, len(words)): # i가 1부터 words의 개수-1까지 반복
    now_W = 0 # 현재의 W 앞으로 채울 수 있는지를 확인하기 위함
    min_penalty = W**3 # min_penalty로 가능한 가장 큰수인 W의 3제곱을 초기값으로 지정
    for j in range(i, -1, -1): # j가 i부터 0보다 크거나 같을 때 까지
        now_W += lenght[j] + 1 # now_W에 단어의 길이와 띄어쓰기인 1을 더해준다.
        if j == 0: # j가 0이라면 패널티에 띄어쓰기로 넣어준 1을 더해주고 W에서 현재의 w를 빼고 3제곱한 값을 넣어준다.
            now_penalty = (W-now_W+1)**3
        else: # j가 0이 아닐때, 현재의 패널티에 전에 계산했던 최소패널티와 방금 계산한 패널티를 더해준다.
            now_penalty = dp[j-1] + (W-now_W+1)**3
        if now_W-1 <= W: # now_W의 값이 W를 넘지 않는다면
            if min_penalty > now_penalty: # now_penalty가 최소패널티라면 
                min_penalty = now_penalty # 최소패널티에 now_penalty를 저장한다.
        else: # now_W값이 W를 넘는다면
            break #while문을 종료하고 i가 1증가한 채로 다시 반복한다.
    dp[i] = min_penalty #dp[i]에 최소패널티를 저장한다.
    #최종적으로 dp[len(words)-1]에 모든 단어를 고려한 최소 패널티가 저장된다.
print(dp[len(words)-1])
# 알고리즘 및 수행시간 설명
# j-1까지의 최소 패널티를 저장하고 이를 다음 계산에 고려하여 계속해서 최소 패널티를
# 구해가는 방식이다. 하지만 계산에 j-2, j-3까지 고려될 필요가 있는 예제가 있고
# 따라서 while을 통해 다시 고려할 수 있도록 해주었다. 리스트의 인덱스 i이면 dp에 i까지의 단어들의
# 최소패널티를 넣는다. 또한 W에 단어가 더 들어갈 수 없으면 바로 계산을 멈춘다. 
# 수행시간은 이중반복문을 사용하고 있는데 하나는 i가 1부터 n까지이고 다른 하나는 i부터 0까지 이므로 
# O(n+(n-1)+(n-2)+(n-3)+...+1) = O((n+1)*n/2) = O(n^2)이다.