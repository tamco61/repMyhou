import schedule
from datetime import datetime
def func():
	h = int(datetime.strftime(datetime.now(), "%H"))
	if h % 12 == 0:
		h = 12
	else:
		h = h % 12
	for i in range(h):
		print('Ку')
schedule.every().hour.at(':00').do(func)
while True:
	schedule.run_pending()