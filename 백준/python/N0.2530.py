hour,min,sec=map(int,input().split())
cooktime=int(input())
sec=sec+cooktime
s=int(sec/60)
sec=int(sec%60)
min=min+s
m=int(min/60)
hour+=m
min=int(min%60)
while(hour>=24):
    hour-=24

print(hour, min, sec)