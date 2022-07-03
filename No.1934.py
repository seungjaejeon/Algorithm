T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    if a>b:
        i=a
    else:i=b
    while(i>1):    
        
        if(a%i==0 and b%i==0):
            print(a*b//i)
            break
        else: i-=1
    if(i<=1):
        print(a*b)
        
