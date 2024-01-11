def solution(clothes):
    answer = 0
    dic = {}
    multi = 1
    result = 0
    for i in clothes:
        if i[1] in dic:
            dic[i[1]].append(i[0])
        else: dic[i[1]] = [i[0]]    
    for i in dic:
        multi *= len(dic[i])+1
    answer = multi-1
    return answer