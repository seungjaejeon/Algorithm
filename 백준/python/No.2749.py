# 피사노 주기
fibo_mem = [0, 1]
n = int(input())
num = 1000000
p = num//10*15
for i in range(2, p):
    fibo_mem.append(fibo_mem[i-1] + fibo_mem[i-2])
    fibo_mem[i] %= num
print(fibo_mem[n%p])