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
```python
import ShellExecution as SE
import sys

cmd = "dir"
result, out = SE.exe(cmd)

if result != 0:
    print("execution error")
    sys.exit(1)

else:
    print(out)
    '''
    output
    hogehoge.exe hello.c test.py
    '''
```