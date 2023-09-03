T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    height = N % H
    weight = N // H + 1
    if height==0:
        weight -= 1
        height = H
    if weight<10:
        weight = '0'+str(weight)
    print(str(height)+str(weight))