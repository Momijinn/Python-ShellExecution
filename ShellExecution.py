# -*- coding:utf-8 -*-
#!/usr/bin/env python
'''
Create by KanameTakano
shellを起動するためのプログラム
このプログラムをインポートし、引数を指定してあげれば起動する

sucsess = 0
false = 1
return 実行は成功したか, 実行結果がくる
'''
import subprocess
import sys

def exe(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()
    out = stdout_data.decode('utf-8').split('\r\n')[0]

    return p.returncode, out


if __name__ == '__main__':
    cmd = "hello.exe"

    result, out = exe(cmd)

    if result != 0:
        print("error")
        sys.exit()

    else:
        print(out)
