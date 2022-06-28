#테스트 케이스 입력
T=int(input())
#테이트 케이스 만큼 반복
for i in range(T):
    #반복횟수와 반복할 문자열 입력받음
    R,S=map(str,input().split())
    #문자열의 길이만큼 반복
    for j in range(len(S)):
        #반복횟수만큼 반복
        for k in range(int(R)):
            print(S[j],end='')
    print("")    
