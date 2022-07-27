from random import randint
# generate_numbers 난수 생성기
def generate_numbers(n):
    num = []
    i = 1
    while i <= n:
        i += 1
        ran = randint(1, 46)
        while ran in num:
            ran = randint(1, 46)        
        num.append(ran)
    return num

        
# draw_winning_numbers 일반 당첨 번호 6개는 정렬 보너스 번호는 마지막에 추가
def draw_winning_numbers():
    numbers = generate_numbers(6)
    numbers.sort()
    
    while len(numbers) < 7:
        ran = randint(1, 46)

        if ran not in numbers:
            numbers.append(ran)

    return numbers

# count_matching_numbers 두 리스트 사이에 겹치는 번호 개수를 리턴한다.
def count_matching_numbers(list_1, list_2):
    same = 0

    for num_1 in list_1:
        if num_1 in list_2:
            same += 1

    return same
# check 참가자의 당첨금액을 리턴함
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    if count == 3:
        return 5000
    elif count == 4:
        return 50000
    elif count == 6:
        return 1000000000
    elif count == 5:
        if count_matching_numbers(numbers, winning_numbers) == 6:
            return 50000000
        else: return 1000000
    else: return 0
