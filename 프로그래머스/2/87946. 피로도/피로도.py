import itertools
def solution(k, dungeons):
    answer = -1
    default_k = k
    # 123 132 213 231 321 312
    # 1234 1243 1324 1342 ~~~~
    for j in itertools.permutations(dungeons,len(dungeons)): # 순열 사용하여 모든 경우
        count =0
        k = default_k
        for i in j:
            if k>=i[0]:
                k-=i[1]
                count += 1
        if count > answer:
            answer = count
    return answer