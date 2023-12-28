from collections import deque
def solution(begin, target, words):
    queue = deque([])
    queue.append([begin, 0])
    visited = [0 for _ in range(len(words))]
    
    while queue:
        word, count= queue.popleft()
        if word == target:
            return count
        for i in range(len(words)):
            match_count = 0
            if visited[i]==1:
                continue
            for j in range(len(word)):
                if words[i][j] != word[j]:
                    match_count += 1
            if match_count==1:
                queue.append([words[i], count+1])
                visited[i]=1
    return 0