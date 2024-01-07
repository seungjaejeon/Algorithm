def solution(s):
    answer = True
    stack = []
    for i in s:
        if stack:
            if stack[-1]=="(" and i==")":
                stack.pop()
            elif stack[-1]=="(" and i=="(":
                stack.append(i)
        else: 
            if i==")":
                return False
            stack.append(i)
    if stack:
        return False
    return True