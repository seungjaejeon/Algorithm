import sys
sound = list(map(int, sys.stdin.readline().split()))
count1 = 0
count2 = 0
for i in range(1,8):
    if sound[i]-sound[i-1]==1:
        count1 += 1
    elif sound[i-1]-sound[i]==1:
        count2 += 1
    
if count1==7:
    print("ascending")
elif count2 == 7:
    print("descending")
else:
    print("mixed")