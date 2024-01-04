def solution(answers):
    answer = []
    count = [0,0,0]
    math1 = []
    math2 = []
    math3 = []
    math2_example = [2,1,2,3,2,4,2,5]
    math3_example = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        math1.append((i%5)+1)
        math2.append(math2_example[(i%8)])
        math3.append(math3_example[(i%10)])
    
    for i in range(len(answers)):
        if math1[i] == answers[i]:
            count[0]+=1
        if math2[i] == answers[i]:
            count[1]+=1
        if math3[i] == answers[i]:
            count[2]+=1
    max_val = max(count)
    for i in range(3):
        if count[i]==max_val:
            answer.append(i+1)
    return answer