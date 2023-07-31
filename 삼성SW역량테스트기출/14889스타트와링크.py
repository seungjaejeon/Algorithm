import sys
import itertools
N = int(sys.stdin.readline())
power = []
for i in range(N):
    power.append(list(map(int,sys.stdin.readline().split())))
power_start = []
team = []
# 조합인거지 NCN/2
# N/2로 나눠서 나올 수 있는 팀의 리스트는 i/i를 기준으로 나눴을 때 나오는 값들이다~ 따라서 조합을 사용한다.
for i in itertools.combinations(range(N),N//2):
    power_team = 0
    for j in itertools.combinations(i,2):
        # 각각의 팀의 능력치의 합
        power_team += power[j[0]][j[1]] + power[j[1]][j[0]]
    print(i,power_team)
    power_start.append(power_team)
power_link = power_start[len(power_start)//2:]
power_start = power_start[:len(power_start)//2]
min_power = float("inf")
# 능력치의 합끼리 뺐을 때 가장 작은 차이를 보이는 것을 return
print(power_start,power_link)
for i in range(len(power_link)):
    min_power = min(min_power, abs(power_start[i] - power_link[len(power_link)-1-i]))
print(min_power)