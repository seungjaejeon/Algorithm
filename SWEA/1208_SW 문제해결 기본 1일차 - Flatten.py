for test_case in range(1, 11):
    dump_count = int(input())
    pan = list(map(int, input().split()))
    def dump(max_index, min_index):
        pan[max_index]-=1
        pan[min_index]+=1
    while dump_count>0:
        max_index = pan.index(max(pan))
        min_index = pan.index(min(pan))
        dump(max_index, min_index)
        dump_count-=1
    print(f'#{test_case} {max(pan)-min(pan)}')