N = int(input())
three_six_nine = ['3','6','9']
for i in range(1,N+1):
    is_three_six_nine = False
    for j in str(i):
        if j in three_six_nine:
            is_three_six_nine = True
            print('-', end="")
    if is_three_six_nine:
        print(end=" ")
    else:
        print(i, end=" ")