# 數字華容道 Digital Klotski
import random
from datetime import datetime

random.seed(datetime.now()) #設定隨機種子
def num2FormatStr(digits, prefix, num): #數字轉含前綴字串
	result = str(num)
	while len(result) < digits:
		result = "%s%s" %(prefix, result)
	return result
def makeSpecMatrix(m_size, last_item):
	result = []
	for i in range(1,(m_size**2)+1):
		result.append(i)
	result = result[:-1]
	result.append(0)
	return result
class DigitalKlotski(object):
	List_LevelName = ('Easy', 'Normal', 'Difficult', 'Hard', 'Expert') # 等級名稱
	List_MatrixSize = (3, 4, 5, 6, 7) # 方陣大小
	List_QuizMoves = (15, 30, 60, 105, 165) # 方陣出題移動數

	def __init__(self, level):
		if isinstance(level, int) and (level > 0 and level <= 5):
			self.configInit(level-1)
		else:
			self.configInit(0)

	def configInit(self, level):
		self.Config = {
			"MatrixLevel": self.List_LevelName[level],
			"MatrixSize": self.List_MatrixSize[level], 
			"QuizMoves": self.List_QuizMoves[level]
		}
		# 建立華容道
		self.Config["Matrix_Goal"] = makeSpecMatrix(self.Config["MatrixSize"],0)
		self.Config["Matrix_Quiz"] = self.Config["Matrix_Goal"].copy()
		self.makeQuizMatrix()

	def makeQuizMatrix(self): # 產生華容道題目
		MOVE = self.Config["QuizMoves"] # 要移動的總次數
		ACT = ['up', 'down', 'left', 'right'] # 要移動的方向集
		RM = ['down', 'up', 'right', 'left'] # 相對應項目集
		action = ACT.copy() # 要移動的候選方向
		while MOVE != 0:
			idx = int(random.random()*len(action))
			mov = action[idx]
			success = self.moveQuizMatrix(mov)
			if success:
				MOVE -= 1
				action = ACT.copy()
				rmAction = RM[action.index(mov)] # 找出要去除的項目(避免原地打轉)
				action.pop(action.index(rmAction))
			else:
				action.pop(idx) # 去除試過的項目

	def getEmptyPos(self): # 取得空格位置
		matrixSize = self.Config["MatrixSize"]
		empty = list(self.Config["Matrix_Quiz"]).index(0)
		emptyPos = [int(empty/matrixSize), empty%matrixSize]
		target = (
			{'pos':[emptyPos[0]-1, emptyPos[1]], 'idx':-1, 'num':-1},
			{'pos':[emptyPos[0]+1, emptyPos[1]], 'idx':-1, 'num':-1},
			{'pos':[emptyPos[0], emptyPos[1]-1], 'idx':-1, 'num':-1},
			{'pos':[emptyPos[0], emptyPos[1]+1], 'idx':-1, 'num':-1}
		)
		for tar in target:
			if (tar["pos"][0] >= 0 and tar["pos"][0] < matrixSize) and (tar["pos"][1] >= 0 and tar["pos"][1] < matrixSize):
				tar["idx"] = (tar["pos"][0]*matrixSize)+tar["pos"][1]
				tar["num"] = self.Config["Matrix_Quiz"][tar["idx"]]
		return matrixSize, empty, target

	def moveQuizMatrix(self, action): # 移動華容道方塊(以空格為主)
		matrixSize, empty, target = self.getEmptyPos()
		ACT = ['down', 'up', 'right', 'left'] # 要移動的方向集
		try:
			actionTarget = target[ACT.index(action)]["idx"]
		except:
			actionTarget = -1
		if target != -1:
			self.Config["Matrix_Quiz"][empty], self.Config["Matrix_Quiz"][actionTarget] = self.Config["Matrix_Quiz"][actionTarget], self.Config["Matrix_Quiz"][empty]
			return True
		else:
			return False

	def moveBlock(self, block): # 玩家移動方塊(以目前方塊為主)
		matrixSize, empty, target = self.getEmptyPos()
		targetBlock = [False, -1] #是否與空格鄰近, 方塊一維位址
		for tar in target:
			if tar['num'] == block:
				targetBlock = [True, tar['idx']]
				break
		if targetBlock[0]:
			self.Config["Matrix_Quiz"][empty], self.Config["Matrix_Quiz"][targetBlock[1]] = self.Config["Matrix_Quiz"][targetBlock[1]], self.Config["Matrix_Quiz"][empty]
			return True
		else:
			return False

	def showQuizMatrix(self): # 顯示華容道
		matrixSize = self.Config["MatrixSize"]
		digits = len(str(max(self.Config["Matrix_Quiz"])))
		bordlen = (digits+1)*matrixSize
		bordLine = "" # 橫向分隔線
		for i in range(bordlen):
			bordLine += '-'

		print(bordLine)
		showStr = ""
		for i in range(len(self.Config["Matrix_Quiz"])):
			if self.Config["Matrix_Quiz"][i] == 0:
				numStr = num2FormatStr(digits, "-", "")
			else:
				numStr = num2FormatStr(digits, "0", self.Config["Matrix_Quiz"][i])
			if i%matrixSize == matrixSize-1:
				showStr += "%s\n" %(numStr)
			else:
				showStr += "%s " %(numStr)
		print(showStr)

	def getQuizMatrix(self): # 顯示題目的陣列
		return tuple(self.Config["Matrix_Quiz"])

	def MatrixFinish(self): # 華容道是否完成(兩陣列完全相同)
		for i in range(len(self.Config["Matrix_Goal"])):
			if self.Config["Matrix_Quiz"][i] != self.Config["Matrix_Goal"][i]:
				return False
		return True