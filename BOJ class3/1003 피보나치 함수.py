import sys
T = int(sys.stdin.readline())
for _ in range(T):
    dp_0 = [1, 0, 1]
    dp_1 = [0, 1, 1]
    N = int(sys.stdin.readline())
    for i in range(3, N+1):
        dp_0.append(dp_0[i-1] + dp_0[i-2])
        dp_1.append(dp_1[i-1] + dp_1[i-2])
    print(dp_0[N], dp_1[N])
    