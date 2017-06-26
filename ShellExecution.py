# -*- coding:utf-8 -*-
#!/usr/bin/env python
'''
Create by KanameTakano
shellを起動するためのプログラム
途中に出力される標準出力に対応した関数も追加
このプログラムをインポートし、引数を指定してあげれば起動する

sucsess = 0
false = 1
return 実行は成功したか, 実行結果がくる

'''

import subprocess
import sys


#途中結果をリアルタイムで出力
def realtime_exe(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = p.stdout.readline()
        if line:
            #適宜変更
            line = line.decode('utf-8').split('\r\n')[0]
            #line = line.decode('shift_jis').split('\r\n')[0]
            yield line

        if not line and p.poll() is not None:
            break


#実行し終えたら結果を出力
def exe(cmd):
    #p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout_data, stderr_data = p.communicate()
    out = stdout_data.decode('utf-8').split('\r\n')[0]
    return p.returncode, out


if __name__ == '__main__':

    print("######exe#####")
    cmd = "python test1.py"

    result, out = exe(cmd)

    if result != 0:
        print("error")
        sys.exit()
    else:
        print(out)


    print("#####realtime_exe#####")
    #バッファーにためないようにするためにすることをすること!
    #https://stackoverflow.com/questions/2804543/read-subprocess-stdout-line-by-line
    #ex) python -u hogehoge.py
    cmd = "python -u test2.py"
    for line in realtime_exe(cmd):
        print(line)