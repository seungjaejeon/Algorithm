from random import randint

def generate_numbers():
    numbers = []

    # 코드를 작성하세요.
    while len(numbers) < 3:
        ran = randint(0, 9)
        if ran not in numbers:
            numbers.append(ran)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        guess = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess)+1)))
        if guess > 9 or guess < -1:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else: new_guess.append(guess)
    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for ball in guesses:
        if ball in solution:
            ball_count += 1
    for strike in range(3):
        if guesses[strike] == solution[strike]:
            strike_count += 1
    ball_count -= strike_count

    return strike_count, ball_count

#게임 시작
ANSWER = generate_numbers()
tries = 0

# 코드를 작성하세요.
while True:
    tries += 1
    guesses = take_guess()
    
    strike_count, ball_count = get_score(guesses, ANSWER)
    print("{}S {}B\n".format(strike_count, ball_count))
    if strike_count == 3:
        break
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
