T = int(input())
for i in range(T):
    result = 0
    ocount = 0
    ox = str(input().strip())
    for j in ox:
        if j=='O':
            ocount += 1
            result += ocount
        else:
            ocount=0
    
    print(result)