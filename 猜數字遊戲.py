# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對印出 "終於猜對了!"
# 猜錯的話，要告訴他 比答案大/小
import random

r = random.randint(1,100)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num > r:
		print('猜得比正確數字大喔~')
	elif num < r:
		print('猜得比正確數字小喔~')
	else:
		print('終於猜對了!')
		break