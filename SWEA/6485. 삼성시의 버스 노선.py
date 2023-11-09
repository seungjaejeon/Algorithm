T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A, B = [], []    
    line = []
    for i in range(N): # 버스 노선
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        
    P = int(input())

    for i in range(P):
        p = int(input())
        line.append([p,0]) # 정류장

    for i in range(N):
        for j in range(A[i],B[i]+1):
            for k, val in enumerate(line):
                if val[0]==j:
                    val[1]+=1

    print(f'#{test_case}',end=" ")
    for i,val in enumerate(line):
        print(val[1], end=" ")
    print()