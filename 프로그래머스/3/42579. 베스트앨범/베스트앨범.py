def solution(genres, plays):
    answer = []
    dic = {} # genre : plays 리스트를 가지는 딕셔너리
    index = {} # index : play 딕셔너리
    name = {}
    sum_genre = []
    for i in range(len(genres)):#dic, name, index dictionary initialize
        if genres[i] in dic:
            dic[genres[i]].append(plays[i])
            name[genres[i]] += plays[i]
        else: 
            dic[genres[i]] = [plays[i]]
            name[genres[i]] = plays[i]
        index[i] = plays[i]
        
    for i in dic:
        dic[i].sort()
        sum_genre.append(sum(dic[i]))
    sum_genre.sort()
    for i in range(len(sum_genre)-1, -1, -1):
        for j in dic:
            if sum_genre[i] == name[j]: # 정렬된 합 뒤에서부터 찾기
                if len(dic[j])>=2: # 장르별 곡이 두개 이상일 경우
                    for k in range(len(dic[j])-1,len(dic[j])-3,-1): # 
                        for t in index:
                            if dic[j][k] ==index[t]:
                                if t not in answer:
                                    answer.append(t)
                else: # 장르별 곡이 하나일경우
                    for t in index:
                            if dic[j][0] ==index[t]:
                                if t not in answer:
                                    answer.append(t)
                                
    return answer