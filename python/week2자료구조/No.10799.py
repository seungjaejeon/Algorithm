import sys
sen = str(sys.stdin.readline().rstrip())
bar = list(sen)
new = []
ba = []
count = 0
for i in bar:
    if i == "(":
        new.append("(")
    else:
        if new[-1] == "(":
            new.pop()
            new.append("0") # 레이저 표시
        else: new.append(")")
# (0)(((0)))0(0) 형태로 변환
for i in new:
    if i == "(":
        ba.append("(")
    elif i == ")":
        ba.pop()
        count += 1
    else:
        count += len(ba)    
print(count)