# Python-ShellExecution
pythonにて外部シェルを簡単に実行できるライブラリ

# 確認した動作環境
* python 2.7
* python 3.5

# 使いかた
ShellExecution.pyをファイルにおき、インポートしてくれれば動きます

# 関数の説明
## 1. exe
    外部シェルが終了したら、正常に実行できたかの有無と実行結果渡します

## 2. realtime_exe
    途中で出力される標準出力結果をリアルタイムで出力します

    これを実行するときは、for文等でループをさせて置いてください

    また、使用環境に応じてライブラリ内の文字コードをを適宜変えてください



# Example
example.py
```python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
import ShellExecution as SE
import sys

print("######exe#####")
cmd = "python test1.py"

result, out = SE.exe(cmd)

if result != 0:
    print("error")
    sys.exit()
else:
    print(out)


print("#####realtime_exe#####")
cmd = "python -u test2.py"
for line in SE.realtime_exe(cmd):
    print(line)
```