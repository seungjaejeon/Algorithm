n = int(input()) # n 입력
bar1 = [[0 for i in range(2)] for j in range(n)] # bar 1 시작점을 저장할 2차원 리스트 생성 (크기: n*2)
bar2 = [[1 for j in range(2)] for k in range(n)] # bar 2 끝나는 점을 저장할 2차원 리스트 생성 (크기: n*2)
for i in range(n):
    bar1[i][0], bar2[i][0] = map(int, input().split()) # bar1, bar2에 i, 0번째 인덱스에 막대의 시작점과 끝점을 각각 입력받음
bar = bar1 + bar2
# bar라는 bar1과 bar2를 합친 리스트 생성
bar.sort() #합친 리스트를 앞자리 (n, 0인덱스)기준으로 정렬함
count = 0 # 꽂힌 막대의 개수를 카운트할 변수 선언
max_count = -1 # 최대 카운트의 개수를 저장할 변수 선언
for i in range(len(bar)): # 0부터 bar의 길이-1 까지
    if bar[i][1] == 0: count += 1 # 0이면 시작점이므로 + 1
    if max_count < count: # 끝나는 점까지 포함되므로 max_count에 저장한 후에 count-1해준다.
        max_count = count
    if bar[i][1] == 1: count -= 1 # 1이면 끝나는 점이므로 -1
print(max_count) # 출력

# 알고리즘 및 수행시간 분석
# 시작점과 끝점에 표기를 해둔다. 시작점은 0으로 끝 점은 1로
# 시작점과 끝점을 합친 리스트를 sort한다. sort 후에 for문을 통해서 bar의 값들을 하나씩 보며 count한다.
# max_count에 그때 그때의 큰값을 저장한다.
# 끝점까지는 막대가 뚫린것으로 간주하기 때문에 max_count에 넣는것을  if bar[i][1] == 1: count -= 1 구문 전에 실행한다.
# 수행시간은 우선 sort하는 것이 n*logn이고 for문이 n이고 for문 내에서 count만 했기 때문에 1이다. 따라서 수행시간은 nlogn + n이므로
# Big-O(n*logn)이다.