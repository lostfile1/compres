import sys
import os
import base64
import zlib

with open(sys.argv[1],'r') as file1:
 data = file1.read()

if sys.argv[2] =="c":
    code = base64.b64encode(zlib.compress(data.encode('utf-8'),8))
    code = code.decode('utf-8')
    f = open('pressed.txt','w')
    f.write(code)
    f.close()
