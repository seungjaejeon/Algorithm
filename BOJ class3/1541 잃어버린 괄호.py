import sys
calculate = str(sys.stdin.readline().strip())
temp = ''
cal = '('
for i, val in enumerate(calculate):
    if val == '+':
        temp = int(temp)
        cal+=str(temp)
        cal+='+'
        temp = ''
    elif val == '-':
        temp = int(temp)
        cal+=str(temp)
        cal+=')'
        cal+='-'
        cal+='('
        temp = '' 
    else:
        temp+=val
temp = int(temp)
cal+=str(temp)
cal+=')'
print(eval(cal))