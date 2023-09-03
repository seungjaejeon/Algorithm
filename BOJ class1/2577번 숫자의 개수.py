A = int(input())
B = int(input())
C = int(input())
result = A*B*C
num = [0 for i in range(10)]
for i in str(result):
    num[int(i)] += 1

for i in num:
    print(i)