import os
path = "C:\PP2\Lab6\Path"
if os.access(path,os.F_OK):
    print(*os.walk(path))