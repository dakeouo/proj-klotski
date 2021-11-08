# 數字華容道 Klotski
from datetime import datetime
from DigitalKlotski import DigitalKlotski

moveTimes = 0 #使用者移動次數

print("================================")
print("==  Welcome to play Klotski!  ==")
print("================================")
print("  Press 'q' to leave this game. ")
print("================================")

inputSize = input("Which Klotski's level would you want to play?(1~5):")
klotski = DigitalKlotski(level=int(inputSize)) # 建立數字華容道
print("OK! Klotski's level will set '%s'." %(klotski.Config["MatrixLevel"]))
print("================================")

# 前置作業
print("== GAME START ==")
klotski.showQuizMatrix() # 顯示題目

# 開始遊戲
startTime = datetime.now()
while not klotski.MatrixFinish():
	key = input("Press block number:")
	try:
		success = klotski.moveBlock(int(key))
	except:
		success = klotski.moveBlock(0)
	if success:
		moveTimes += 1
	print("Moves:", moveTimes)
	klotski.showQuizMatrix() # 顯示題目

	if str(key) == "q" or str(key) == "Q":
		break

# 遊戲結算
endTime = datetime.now()
time_s = (endTime - startTime).seconds
time_ms = (endTime - startTime).microseconds
fullsec = time_s + float(str("0.%d" %(time_ms)))
if klotski.MatrixFinish():
	print("Congratulation! you move %d times to finish this game." %(moveTimes))
else:
	print("You are not finish yet!")
print('Spend Time (sec):', "%.3fms" %(fullsec))