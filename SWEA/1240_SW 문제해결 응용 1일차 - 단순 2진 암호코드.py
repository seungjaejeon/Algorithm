from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pan = []
    for i in range(N):
        line = input().strip()
        pan.append(line) #입력받기
    sentence = deque() # 암호화된 56자리 비트를 저장할 리스트
    for i in range(N):
        for j in range(M-1,-1,-1): # 뒤에서부터 1인값을 찾는다. 모든 56자리비트 암호문은 마지막에 1로 끝나기때문에
            if pan[i][j]=='1':
                for k in range(j,j-56,-1):
                    sentence.appendleft(pan[i][k])
                break
        if len(sentence)!=0: # 이미 찾았으면 break
            break
    string = '' #7자리비트 저장할 변수
    string_ex = ['0001101', '0011001', '0010011','0111101', '0100011', '0110001', '0101111','0111011','0110111','0001011'] # 암호문 리스트
    decode = [] # 복호화한 값 들어갈 리스트
    for i in range(1, 57):
        string += sentence[i-1] #7자리까지
        if i%7==0: # 7자리마다
            for j in range(10): 
                if string == string_ex[j]: # 암호문에 해당하는 값이 있는지 확인
                    decode.append(j) # decode리스트에 복호화한 값 append
                    break
            string='' # 7자리 체크 끝났기 때문에 다시 초기화
    result = 0 # 짝수자리 값 더할 변수 및 최종 합 저장할 변수
    result_odd = 0 # 홀수자리 값 더할 변수
    for i, val in enumerate(decode):
        if i%2==0: #홀수자리이면
            result_odd+=val
        else: #짝수자리이면
            result+=val
    result = result+(result_odd*3) # 홀수자리만 3곱하고 더하기
    if result%10==0: #올바른 암호문이라면
        print(f'#{test_case} {sum(decode)}')
    else: # 올바리지 않은 암호문이라면
        print(f'#{test_case} 0')