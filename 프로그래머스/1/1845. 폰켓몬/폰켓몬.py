def solution(nums):
    answer = 0
    dic = {}
    N = len(nums)/2
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    if N<len(dic.keys()):
        answer = N
    else:
        answer = len(dic.keys())
    return answer
#n/2가져가라
#같은 종류의 폰켓몬은같은 번호를 가지고 있음
# 3 1 2 3 -> 3번 2마리 1번 한마리 2번 한마리
