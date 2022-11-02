hour,min=map(int,input().split())
cooktime=int(input())
min=min+cooktime
h=int(min/60)
hour+=h
min=min-(h*60)
if(hour>=24):
    hour-=24
print(hour, min) 