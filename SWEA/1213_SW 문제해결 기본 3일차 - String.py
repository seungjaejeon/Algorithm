for _ in range(10):
    test_case = int(input())
    find = input()
    string = input()
    answer = 0
    for i, val in enumerate(string):
        is_equal = False
        if val == find[0]:
            for j in range(i,i+len(find)):
                if j<=len(string)-1:
                    if string[j]==find[j-i]:
                        is_equal = True
                    else:
                        is_equal = False
        if is_equal==True:
            answer += 1

    print(f'#{test_case} {answer}')