# 1. () 를 확인한다.

# 2.  * /인지를 확인하고 먼저 들어온, 같은 우선순위에 있는 * / 는 모두 결과문자열에 추가해준다.

# 3. 그리고 현재 문자를 다시 스택에 추가

# 4. +, - 인지 확인한다. + ,- 는 이들보다 낮은 우선순위의 연산자가 없으므로 자신보다 우선순위가 높은 것들을 모두 

# 결과 문자열에 추가해준다.

# 5. ) 를 발견하면 ( 와 ) 사이에 있는 모든 연산자들을 결과문자열에 추가하고 (를 pop해준다.

# 그리고 마지막으로 남아있는 stack을 pop하며 결과문자열에 추가해주면 끝.
strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)