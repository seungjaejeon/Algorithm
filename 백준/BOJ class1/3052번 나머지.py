num = dict()
for i in range(10):
    n = int(input())
    if n%42 not in num:
        num[n%42]=0
    else:
        num[n%42]+=1
print(len(num))