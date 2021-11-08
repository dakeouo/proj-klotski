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