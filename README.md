# klotski-app
數字華容道 (Digital Klotski)

## [Stage1] Python
### Prepare
Docker Image Version: 1.x
- Pull docker image:
```bash
docker pull gcp852/klotski-app:1.x
```
- Execute program at Terminal:
```bash
Python app.py
```

### Excute
- Welcome view:
```bash
================================
==  Welcome to play Klotski!  ==
================================
  Press 'q' to leave this game.
================================
Which Klotski's level would you want to play?(1~5):
```
- Playing view:
```bash
Moves: 3
------------
01 03 04 12
05 02 07 15
14 09 08 06
13 10 -- 11

Press block number:
```
- Finish view:
```bash
Congratulation! you move 5 times to finish this game.
Spend Time (sec): 12.843ms
```

## [Stage2] Flask
### Prepare
Docker Image Version: 2.x
-- Pull docker image:
```bash
docker pull gcp852/klotski-app:2.x
```
-- Setting flask envirment:
 - Linux：`export FLASK_APP=app.py`
 - Windows：`set FLASK_APP=app.py`

-- Execute program at Terminal:
1. `flask run --reload --debugger --host 0.0.0.0 --port 80`
2. `python app.py`

### Excute
- Welcome view:

![Imgur](https://i.imgur.com/BNQ3hvu.png)

- Playing view:

|![Imgur](https://i.imgur.com/3p0dSfx.png)|![Imgur](https://i.imgur.com/98QF4oK.png)|![Imgur](https://i.imgur.com/jr5b7vh.png)|
| ------ | ------ | ------ |
| Game Start | Game Play | Game Finish |