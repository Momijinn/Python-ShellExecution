# Python-ShellExecution
pythonにて外部シェルを簡単に実行できるライブラリ

# 確認した動作環境
* python 2.7
* python 3.5

# 使いかた
このプログラムをファイルにおき、インポートしてくれれば動きます

引数が2つ出ます

1. 実行が成功したかの有無

    * 0 : 実行成功
    * それ以外 : 実行失敗

2. 実行結果

    *実行結果が来ます(print等で出力したものでてくるので注意)


# Example
example.py
```python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
import ShellExecution as SE
import sys

cmd = "hello_world.exe"


result, out = SE.exe(cmd) #SE.exe(execution)

if result != 0:
    print("error")
    sys.exit()

else:
    print(out) #hello_world
```