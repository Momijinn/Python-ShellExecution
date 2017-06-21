# -*- coding:utf-8 -*-
#!/usr/bin/env python
import ShellExecution as SE
import sys

cmd = "hello_world.exe"

'''
result: 0(success) or 1(failed)
out:Execution result
'''
result, out = SE.exe(cmd) #SE.exe(execution)

if result != 0:
    print("error")
    sys.exit()

else:
    print(out) #hello_world