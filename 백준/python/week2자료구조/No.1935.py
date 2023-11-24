import sys
N = int(sys.stdin.readline())
sen = sys.stdin.readline().rstrip()
sen2 = list(sen)
num = []
newsen = []
for i in range(N):
    num.append(int(sys.stdin.readline()))
for i in sen2:
    if ord(i)<=90 and ord(i)>=65:
        newsen.append(num[ord(i)-65]) 
    else:
        a = float(newsen.pop()) #연산자 전의 숫자
        b = float(newsen.pop()) #연산자 전전의 숫자
        if ord(i) == 43: # +
            newsen.append(b+a)
        elif ord(i) == 45: # -
            newsen.append(b-a)
        elif ord(i) == 47: # /
            newsen.append(b/a)
        elif ord(i) == 42: # *
            newsen.append(b*a)
print("%.2f" %newsen[0])
