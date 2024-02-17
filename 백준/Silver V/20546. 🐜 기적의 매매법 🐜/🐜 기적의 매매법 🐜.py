import sys
start = int(sys.stdin.readline())
prices = list(map(int, sys.stdin.readline().split()))

def junhyeon(money, price):
    global purchase_jun
    if money>=price:
        purchase = money//price
        money -= purchase*price
        purchase_jun += purchase
    return money # 남은 돈

def sungmin(money, yesterday_price, price, stack):
    global purchase_sung
    if stack>=0 and price-yesterday_price>0:
        stack += 1
    if stack<=0 and price-yesterday_price<0:
        stack-=1
    if stack<=0 and price-yesterday_price>0:
        stack = 1
    if stack>=0 and price-yesterday_price<0:
        stack = -1

    if stack>=3:
        money += purchase_sung * price
        purchase_sung = 0
        # 전량 매도
    elif stack<=-3:
        purchase = money//price
        money -= purchase*price
        purchase_sung += purchase
        # 전량 매수
    return money, stack

start_jun = start
start_sung = start
purchase_jun = 0
purchase_sung = 0
stack = 0
yesterday_price = prices[0]
for i in prices:
    start_jun = junhyeon(start_jun, i)
    start_sung, stack = sungmin(start_sung, yesterday_price, i, stack)
    yesterday_price = i

money_jun = start_jun + yesterday_price*purchase_jun
money_sung = start_sung + yesterday_price*purchase_sung 
if money_jun>money_sung:
    print("BNP")
elif money_jun<money_sung:
    print("TIMING")
elif money_jun==money_sung:
    print("SAMESAME")