# 數字華容道 Klotski
from flask import Flask, render_template, redirect
from datetime import datetime
from DigitalKlotski import DigitalKlotski

app = Flask(__name__)

GAME_MOVETIMES = 0 #使用者移動次數
GAME_OBJECT = "NULL" #遊戲物件
GAME_STATE = 0 #遊戲狀態(0=初始/1=開始/2=暫停)

@app.route('/')
def index():
	global GAME_OBJECT
	GAME_OBJECT = "NULL"
	return render_template('index.html')

@app.route('/klotski/<int:lv>')
def klotski(lv):
	global GAME_OBJECT, GAME_STATE, GAME_MOVETIMES
	if isinstance(GAME_OBJECT, str):
		GAME_MOVETIMES = 0
		GAME_STATE = 0
		GAME_OBJECT = DigitalKlotski(level=int(lv)) # 建立數字華容道

	config = {
		"lvid": lv,
		"Level": GAME_OBJECT.Config['MatrixLevel'],
		"Name": "{0} Klotski ({1}x{1})".format(
			(GAME_OBJECT.Config['MatrixSize']**2) - 1, 
			GAME_OBJECT.Config['MatrixSize']
		),
		"Size": GAME_OBJECT.Config['MatrixSize'],
		"Quiz": GAME_OBJECT.getQuizMatrix()
	}
	games = {
		"state": GAME_STATE,
		"movetimes": GAME_MOVETIMES
	}
	return render_template('klotski.html', config=config, games=games)

@app.route('/blocks/<int:key>/<int:lv>')
def blocks(key,lv):
	global GAME_OBJECT, GAME_MOVETIMES
	success = GAME_OBJECT.moveBlock(int(key))
	if success:
		GAME_MOVETIMES += 1
	return redirect('/klotski/%d'%(int(lv)))

@app.route('/gamectl/<string:action>/<int:lv>')
def gamectl(action,lv):
	print(action,lv)
	global GAME_STATE, GAME_MOVETIMES, GAME_OBJECT
	if str(action) == "start":
		GAME_STATE = 1
	elif str(action) == "pause":
		GAME_STATE = 2
	elif str(action) == "stop":
		GAME_MOVETIMES = 0
		GAME_STATE = 0
		GAME_OBJECT = DigitalKlotski(level=int(lv)) # 建立數字華容道
	return redirect('/klotski/%d'%(int(lv)))

if __name__ == "__main__":
	app.run(debug=True)