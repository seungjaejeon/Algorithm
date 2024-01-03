def solution(brown, yellow):
    answer = []
    all_carpet = brown + yellow
    for i in range(1,int(all_carpet**(1/2))+1):
        garo = all_carpet/i
        sero = i
        if yellow == (garo-2)*(sero-2):
            answer.append(garo)
            answer.append(sero)
    return answer