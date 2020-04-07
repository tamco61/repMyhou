from datetime import datetime
import schedule
def func():
    global word, check_lst
    h = int(datetime.strftime(datetime.now(), "%H"))
    if h % 12 == 0:
        v = 12
    else:
        v = h % 12
    if h not in check_lst:
        for i in range(v):
            print(word)
print('Введите сообщение для кукушки:')
word = input()
print('Введите диапозон молчания("hh-hh"):')
check = [int(i) for i in input().split('-')]
check_lst = list()
if check[0] > check[1]:
    check[1] += 24
for i in range(abs(check[1] - check[0]) + 1):
    check_lst.append((check[0] + i) % 24)
schedule.every().hour.at(':00').do(func)
while True:
    schedule.run_pending()