import sys
string = str(sys.stdin.readline().rstrip())
li = list(string)

def fast_string(part_string, f_or_b, before_index):
    if len(part_string)<=0:
        return
    fast_chr = min(part_string)
    index = part_string.index(fast_chr)
    if f_or_b=='b':
        result.insert(before_index+1, fast_chr)
        next_index = before_index + 1
    elif f_or_b == 'f':
        result.insert(before_index, fast_chr)
        next_index = before_index
    for i in result:
        print(i, end='')
    print()
    fast_string(part_string[index+1:], 'b', next_index) # 뒤
    fast_string(part_string[:index],'f', next_index) # 앞
    
    
    # 문자열 중 사전 순으로 가장 빠른 문자를 찾고 그 뒤를 끝낸 뒤에 앞을 끝내기

result = []
fast_string(li,'f',0)
