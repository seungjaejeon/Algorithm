dic = [0 for i in range(27)]
string = str(input().strip())
for i in string.upper():
    dic[ord(i)-65] += 1
count = 0
max_count = max(dic)
max_i = 0
for i in range(26):
    if max_count==dic[i]:
        count += 1
        max_i = i

if count==1:
    print(chr(max_i+65))
else:
    print("?")