import LCD1602
import time

def setup():
	LCD1602.init(0x27, 1)
	LCD1602.write(0,0, 'You guys')
	LCD1602.write(1,1, 'are useless')
	time.sleep(2)
def destroy():
	LCD1602.clear()
if __name__ == '__main__':
	try:
		setup()
	except KeyboardInterrupt:
		destroy()

