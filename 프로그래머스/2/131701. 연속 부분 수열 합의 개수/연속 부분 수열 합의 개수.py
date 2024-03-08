def solution(elements):
    ll = len(elements)
    res = set()
# 핵빠른코드
    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)