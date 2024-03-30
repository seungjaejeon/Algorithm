import sys
n = int(sys.stdin.readline())
pan = [0 for i in range(n)]
def nqueen(k):
    global answer
    if k >= n:
        answer += 1
        return
    for i in range(n):
        pan[k] = i
        if can_place(k, i):
            nqueen(k+1)
        else:
            continue
# 0 0 0 0
# 0 0 0 0 
# 0 0 0 0
# 0 0 0 0
def can_place(k, x):
    for i in range(k):
        if x == pan[i] or abs(k-i) == abs(x-pan[i]): # 일직선
            return False
    return True
answer = 0
nqueen(0)
print(answer)