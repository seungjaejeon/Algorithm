def solution(tickets):
    answer = []
    dic = dict([])
    
    N = len(tickets)
    visited = [False for i in range(N)]
    for i, val in enumerate(tickets):
        if val[0] not in dic:
            dic[val[0]] = [(i, val[1])]
        else:
            dic[val[0]].append((i,val[1]))
    for i in dic.keys():
        dic[i].sort(key = lambda x: x[1])
        
    def dfs(city, path):
        nonlocal answer
        if answer:
            return
        if len(path) == N+1:
            answer = path.copy()
            return
        if city not in dic:
            return
        for i, val in enumerate(dic[city]):
            ni, next_c = val
            if visited[ni]==True:
                continue
            visited[ni] = True
            path.append(next_c)
            dfs(next_c, path)
            path.pop()
            visited[ni] = False
    
    dfs("ICN", ["ICN"])
    return answer
