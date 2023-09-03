string = str(input().strip())
alpha = [-1 for i in range(26)]
for i,val in enumerate(string):
    if alpha[ord(val)-97]==-1:
        alpha[ord(val)-97] = i

for i in range(26):
    print(alpha[i], end=" ")