#테스트 케이스 개수
T=int(input())
#테스트 케이스 만큼 실행
for i in range(T):
    #입력
    b=list(map(str,input().split()))
    #가장 첫번째 숫자 따로 저장
    a=float(b[0])
    #연산
    for j in range(len(b)):
        if(b[j]=="@"):
            a*=3
        elif (b[j]=="%"):
            a+=5
        elif(b[j]=="#"):
            a-=7
    #출력
    print("%0.2f" % a)
    #테스트 하나 끝 다시 반복