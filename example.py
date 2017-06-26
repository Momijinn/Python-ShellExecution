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
#バッファーにためないようにするためにすることをすること!
#https://stackoverflow.com/questions/2804543/read-subprocess-stdout-line-by-line
#ex) python -u hogehoge.py
cmd = "python -u test2.py"
for line in SE.realtime_exe(cmd):
    print(line)