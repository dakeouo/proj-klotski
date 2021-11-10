# 數字華容道 Klotski
import config
from flask import Flask, render_template, redirect
from datetime import datetime
from DigitalKlotski import DigitalKlotski

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

GAME_MOVETIMES = 0 #使用者移動次數
GAME_OBJECT = "NULL" #遊戲物件
GAME_STATE = 0 #遊戲狀態(0=初始/1=開始/2=暫停/3=完成)
GAME_TOTAL_TIME = 0.0 #遊戲花費時間

TIMER_START = datetime.now()
def updateGameTimer():
	global TIMER_START, GAME_TOTAL_TIME
	spendTime = (datetime.now() - TIMER_START)
	time_s = spendTime.total_seconds()
	time_ms = spendTime.microseconds
	full_sec = float(time_s) + float(str("0.%d" %(time_ms)))
	GAME_TOTAL_TIME += full_sec
	return float("%.1f" %(GAME_TOTAL_TIME))

def time2Str(float_time):
	times = float_time*10
	ms = times%10
	sec = int((times/10)%60)
	min_ = int((times/10)/60)
	return "%02d:%02d.%01d" %(min_,sec,ms)

@app.route('/')
def index():
	global GAME_OBJECT
	GAME_OBJECT = "NULL"
	return render_template('index.html')

@app.route('/klotski/<int:lv>')
def klotski(lv):
	global GAME_OBJECT, GAME_STATE, GAME_MOVETIMES, GAME_TOTAL_TIME
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
		"movetimes": GAME_MOVETIMES,
		"timer": GAME_TOTAL_TIME,
		"showtimes": time2Str(GAME_TOTAL_TIME)
	}
	return render_template('klotski.html', config=config, games=games)

@app.route('/blocks/<int:key>/<int:lv>')
def blocks(key,lv):
	global GAME_OBJECT, GAME_STATE, GAME_MOVETIMES, GAME_TOTAL_TIME, TIMER_START
	success = GAME_OBJECT.moveBlock(int(key))
	if success:
		GAME_MOVETIMES += 1
	if GAME_OBJECT.MatrixFinish():
		GAME_STATE = 3
	else:
		GAME_TIMER = updateGameTimer()
	TIMER_START = datetime.now()
	return redirect('/klotski/%d'%(int(lv)))

@app.route('/gamectl/<string:action>/<int:lv>')
def gamectl(action,lv):
	global GAME_STATE, GAME_MOVETIMES, GAME_OBJECT, GAME_TOTAL_TIME, TIMER_START
	if str(action) == "start":
		TIMER_START = datetime.now()
		GAME_TOTAL_TIME = updateGameTimer()
		GAME_STATE = 1
	elif str(action) == "pause":
		GAME_TOTAL_TIME = updateGameTimer()
		GAME_STATE = 2
	elif str(action) == "stop":
		GAME_TOTAL_TIME = 0
		GAME_MOVETIMES = 0
		GAME_STATE = 0
		GAME_OBJECT = DigitalKlotski(level=int(lv)) # 建立數字華容道
	elif str(action) == "restart":
		GAME_TOTAL_TIME = 0
		GAME_MOVETIMES = 0
		GAME_STATE = 1
		GAME_OBJECT = DigitalKlotski(level=int(lv)) # 建立數字華容道
	return redirect('/klotski/%d'%(int(lv)))

if __name__ == "__main__":
	app.run(debug=True)