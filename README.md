Python-ShellExecution
====
pythonにて外部シェルを簡単に実行できるライブラリ

## Description
pythonにて外部ファイルを実行するだけでなく、標準出力結果をリアルタイムで出力をするライブラリ

## Requirement
* 動作確認したpython
    * python 2.7
    * python 3.5

## Usage
1. exe

    外部シェルが終了したら、正常に実行できたかの有無と実行結果渡します
    ```python
    result, out = SE.exe(cmd)
    ```

2. realtime_exe

    途中で出力される標準出力結果をリアルタイムで出力します

    これを実行するときは、for文等でループをさせて置いてください

    また、使用環境に応じてライブラリ内の文字コードをを適宜変えてください

    ```python
    cmd = "python -u test2.py"
    for line in SE.realtime_exe(cmd):
        print(line)
    ```


## Install
```python
import ShellExecution as SE
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Twitter](https://twitter.com/momijinn_aka)

[Blog](http://www.autumn-color.com/)