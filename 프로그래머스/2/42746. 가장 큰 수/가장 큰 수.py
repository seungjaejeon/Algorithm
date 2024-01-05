def solution(numbers):
    # 1. Convert any number to string
    numbers = list(map(str, numbers))

    # 2. Sort by comparing x+y to y+x
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    # 3. Concatenate the sorted numbers and return
    answer = ''.join(numbers)

    # Exception handling to return "0" instead of "000" when there are multiple 0's
    if answer[0] == '0':
        return '0'
    else:
        return answer