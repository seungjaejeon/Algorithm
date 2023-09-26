T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    b = N*N
    count = 0
    for i in range(N+1):
        for j in range(N+1):
            if i*i+j*j<=b:
                count += 1
    count -= N
    count *= 4
    print(count-3)