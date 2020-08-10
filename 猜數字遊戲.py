# 產生一個隨機整數1~100
# 讓使用者重複輸入數字去猜
# 猜對印出 "終於猜對了!"
# 猜錯的話，要告訴他 比答案大/小
import random

r = random.randint(1,100)
count = 0
while True:
	count += 1 # count =count + 1 快捷法
	num = input('請猜數字:')
	num = int(num)
	if num > r:
		print('猜得比正確數字大喔~')
	elif num < r:
		print('猜得比正確數字小喔~')
	else:
		print('終於猜對了!居然猜了',count,'次')
		break
	print('這是你猜的第', count, '次')	