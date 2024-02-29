def solution(edges):
    answer = []
    dic = dict()
    max_val = 0
    for edge in edges:
        if max_val < max(edge):
            max_val = max(edge)
        if edge[1] not in dic:
            dic[edge[1]] = []
        if edge[0] not in dic:
            dic[edge[0]] = [edge[1]]
        else:
            dic[edge[0]].append(edge[1])
    candidate = []
    visited = [0 for i in range(max_val+1)]
    
    for i in dic.values():
        for j in i:
            visited[j] = 1
    for i in dic:
        if len(dic[i]) <= 1:
            visited[i] = 1
    for i, val in enumerate(visited):
        if i!=0 and val == 0:
            created_node = i
    result = [0 for i in range(4)]
    visited = [0 for i in range(max_val+1)]
    # 막대의 특징
    # 마지막에 어디로도 가지 않음
    # 도넛의 특징
    # 순환하여 결국 1로 돌아옴
    # 팔자의 특징
    # 순환하여 결국 1로 돌아옴 2개의 간선이 나가는 노드가 있음
    def dfs(val):
        start = val
        visited[start] = 1
        stack = [val]
        while stack:
            cur = stack.pop()
            
            if len(dic[cur])==0: # 막대 모양
                result[2] += 1
                return
            if len(dic[cur])==1:
                if visited[dic[cur][0]]==0:
                    stack.append(dic[cur][0])
                else:
                    result[1] += 1
                    return
            if len(dic[cur])==2:
                result[3] += 1
                return
            
    # 나가는게 2개인게 중심
    
    result[0] = created_node
    for i in dic[created_node]:
        dfs(i)

                
    return result