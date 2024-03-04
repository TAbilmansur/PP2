import os
path = "C:\PP2\Lab6\\ToDelete.txt"
if (os.access(path,os.F_OK) and os.access(path,os.R_OK) and os.access(path,os.W_OK) and os.access(path,os.X_OK)):
    os.remove(path)
else:
    print("No file found")