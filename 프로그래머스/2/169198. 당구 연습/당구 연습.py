def solution(m, n, startX, startY, balls):
    result = []

    def calDistance(a,b,x,y):
        d = (x-a)**2 + (y-b)**2
        return d
    for i in range(len(balls)):
        min_d = float("inf")
        if startX != balls[i][0] or startY < balls[i][1]: # 아래에 적구가 있음
            min_d = min(min_d,calDistance(startX, startY, balls[i][0], -balls[i][1]))
        if startX != balls[i][0] or startY > balls[i][1]:
            min_d = min(min_d,calDistance(startX, startY, balls[i][0], n+n-balls[i][1]))
        if startY != balls[i][1] or startX < balls[i][0]:
            min_d = min(min_d,calDistance(startX, startY, -balls[i][0], balls[i][1]))
        if startY != balls[i][1] or startX > balls[i][0]:
            min_d = min(min_d,calDistance(startX, startY, m+m-balls[i][0], balls[i][1]))
        result.append(int(min_d))
    return result