## baekjoon in python

round(숫자,반올림 자릿수) # 반올림 함수

# 문자열 연산
hello+hello # hellohello

hello * 3 # hellohellohello

# 형 변환
float(3) # 3.0

float("1.1")# 1.1

# format method
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day)) #format방식

date_string = "오늘은 {}년 {}월 {}일입니다.

print(date_string.format(year, month, day))

# format method 2
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌게이츠"))

#저는 유재석, 박지성, 빌게이츠를 좋아합니다!

{:.2f} #반올림 자릿수

# type함수

type(3) # class 'int'

type(3.0) # class 'float'

type("3") # class 'str'

type(True) # class 'bool'

# 옵셔널 파라미터

코드의 마지막에 들어가야 하며 기본값이라고 생각하면 된다.

# scope

로컬변수와 글로벌변수의 차이를 알아야 한다.

# 스타일 규칙
StarCraft (x)

star_craft (o)

함수 정의 위아래로 빈 줄이 두 개씩 있어야 한다.

괄호 안에는 띄어쓰기를 하지 마라.

(x, y)

코멘트 사용 시 띄어쓰기 최소 두 개를 하기.
  
# list
ex) numbers=[2, 3, 5]

print(numbers[-1]) #5가 출력됨

  리스트 슬라이싱
 
  numbers[:2] #[2, 3]
  
## 리스트 함수

len() #리스트의 길이

numbers.append(5) #numbers리스트에 5를 추가함

del numbers[3] #numbers리스트의 3번 인덱스를 삭제하겠다.

numbers.insert(4,37)#4번 인덱스에 37이라는 값을 추가하겠다.

## 리스트 정렬

sorted(numbers) #작은순으로 정렬

sorted(numbers, reverse=True) #큰순서대로 정렬

sorted함수는 기존의 함수를 건드리지 않는다. 

반면 numbers.sort()는 numbers리스트 자체를 정렬한다.

numbers.sort(reverse=True)는 큰순으로 정렬한다.

numbers.reverse() #원소들을 뒤집어버린다.

numbers.remove(3) #원소들중 가장 첫 번째로 파라미터의 값을 갖고 있는 원소를 삭제한다.
## 리스트내에 값이 있는지를 확인하기

primes = [2, 3, 5, 6, 7, 11]

print(7 in primes) #True

print(12 in primes) #False

print(7 not in primes) #False

print(12 not in primes) # True

## 리스트 안의 리스트(2차원 배열?)

grades = [[62, 75, 77], [78, 81, 86]]

# for문

for index in list:
  
  print(index)
  
# range

for i in range(3, 11) # 3~10까지 start부터 stop-1까지

for i in range(10) # 0부터 9까지

for i in range(start, stop, step) # step은 숫자들 간의 간격을 말한다.
start부터 stop-1까지 step의 간격으로!

# 사전 (dictionary) 키-값 쌍
my_dictionary = {

    5: 25,
    
    2: 4,
    
    3: 9
    
}

print(my_dictonary[3]) # 9출력됨

my_dictionary[9] = 81 #9: 81입력됨

사전의 키는 꼭 정수일 필요가 없음

# 사전 활용법

print('이지영' in my_family.values()) # True

for value in my_family.values(): #값들을 출력
    
    print(value)
    
for key in my_family.keys(): #키들을 받아옴

for key, value in my_family.items():
    
    print(key, value) # 키와 값들을 전부 출력
    
# Aliasing

x = 3

x = y

y = 5

print(y) #5출력됨


x = {2, 3, 5, 7, 10}

y = x

y[2] = 4

print(x) #{2, 3, 4, 7, 10}이 출력됨 이 떄 y = list(x)를 사용했다면 x의 복사본을 y라고 지정한것이므로 y의 값을 바꿔도 x의 값이 바뀌지 않음

# 문자열과 리스트의 공통점과 차이점

두 자료형은 공통적으로 인덱싱이 가능하다.

또한 슬라이싱 역시 가능하다.

덧셈 연산은 연결하는 연산이다.

len함수를 사용가능하다.

문자열과 리스트가 매우 흡사하지만 문자열은 수정이 불가능하고 리스트는 값의 수정이 가능하다.

# module

import calculator # calculator 모듈을 불러오겠다.

사용방법: calculator.add(x, y)

import calculator as calc  #calculator 모듈을 calc로 부르겠다.

calc.add(x, y)

from clacualtor import add, multiply # calculator 모듈에서 add, multiply 함수를 불러오겠다.

add(x, y)

# 스탠다드 라이브러리(standard library)

ex) import math

math.log10(100)

math.cos(0)

math.pi

ex) import random

random.random() # 0.0과 1.0사이의 랜덤한 수를 가져옴

randint 함수

randint는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수입니다.

randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴하는 것이죠.

uniform 함수

uniform은 두 수 사이의 랜덤한 소수를 리턴하는 함수입니다. randint와 다른 것은 리턴하는 값이 정수가 아니라 소수라는 점입니다.

uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴하는 것이죠.

ex) import os

os.getlogin() #어떤 계정으로 로그인 되어있는가

os.getcwd() # 현재 이 파일이 있는 폴더의 경로

ex) import datetime

스탠다드 라이브러리에 있는 datetime 모듈은 '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갖추고 있습니다. 

2020년 3월 14일을 파이썬으로 어떻게 표현할 수 있을까요? 이렇게 하면 됩니다.

    pi_day = datetime.datetime(2020, 3, 14)

    print(pi_day)

    print(type(pi_day))

    2020-03-14 00:00:00

    <class 'datetime.datetime'>

보시다시피 시간은 자동으로 00시 00분 00초로 설정되었는데요. 우리가 시간까지도 직접 정할 수 있습니다.

    pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)

    print(pi_day)

    print(type(pi_day))

    2020-03-14 13:06:15

    <class 'datetime.datetime'>

우리가 날짜와 시간을 정해 주는 게 아니라, 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아 오고 싶다면? 이렇게 하면 됩니다.

    today = datetime.datetime.now()
    
    print(today)
    
timedelta
    두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됩니다.

    today = datetime.datetime.now()
    
    pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
    
    print(today - pi_day)
    
    print(type(today - pi_day))
    
    22 days, 4:42:57.360266
    
    <class 'datetime.timedelta'>
    
# input

사용자가 입력하는 것은 항상 문자열로 취급된다.

따라서 int를 씌워줘야된다.

# 파일 읽기

with open('chicken.txt', 'r') as f:

# strip

print(" \t    \n   abc    bcd     ".strip()) # abc   bcd출력됨 앞뒤의 공백을 없애주는 함수

# split

my_string = "1. 2. 3. 4. 5. 6"

print(my_string.split(". "))

출력: 1,2,3,4,5,6

split은 문자열을 리스트로 만들어 준다. 이 때의 리스트 값들은 모두 문자형이다. str

# 파일 쓰기

    with open('new file.txt', 'w') as f: 
        f.write("Hello World\n")
        
w가 아니라 a를 사용할 경우 그 이름의 파일에 내용을 추가한다. 만약 그 이름의 파일이 없다면 새로운 파일을 만든다.
        
