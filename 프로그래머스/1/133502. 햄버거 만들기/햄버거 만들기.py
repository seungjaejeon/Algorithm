def solution(ingredient): # 스택구조
    answer = 0
    cook = []
    hambuger = [1,2,3,1]
    for i in ingredient:
        cook.append(i)
        if len(cook) >= 4:
            if cook[-4:] == hambuger:
                del cook[-4:]
                answer += 1
    return answer