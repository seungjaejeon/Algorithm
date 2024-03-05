def solution(targets):
    answer = 1
    targets.sort(key=lambda x: (x[1], x[0]))
    start, end = targets[0]
    check = [0 for i in range(len(targets))]
    def if_a_and_b(target1, target2): # 2가 1과 겹치는 부분이 있는가?
        if target1[1] <= target2[0] or target2[1] <= target1[0] :
            return False
        else:
            return True
    for i in range(1, len(targets)):
        # 하나의 타겟이 추가 될 때 가장 짧은 라인에 포함 되어 있는지 확인
        if if_a_and_b([start, end], targets[i]):
            continue
        else:
            answer += 1
        start, end = targets[i]
    return answer