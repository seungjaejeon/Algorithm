T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    # y = -x + a임을 이용
    a_p = 0
    a_q = 0
    for i in range(200):
        if p > 0:
            p = p-i # 그 라인에서 몇번째에 위치한지를 알 수 있음
            a_p = i # 몇번째라인에 위치한지 알 수 있음
        if q > 0:
            q = q-i
            a_q = i
    
    p_x = a_p + p
    p_y = abs(p)+1
    q_x = a_q + q
    q_y = abs(q)+1

    result_x = p_x+q_x
    result_y = p_y+q_y
    result = 0
    len_res = result_x+result_y
    for i in range(len_res-1):
        result += i
    result += result_x
    print(f'#{test_case} {result}')