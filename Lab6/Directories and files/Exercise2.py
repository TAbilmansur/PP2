import os
print(os.access("C:\PP2\Lab6\y.txt",os.F_OK))
print(os.access("C:\PP2\Lab6\y.txt",os.R_OK))
print(os.access("C:\PP2\Lab6\y.txt",os.W_OK))
print(os.access("C:\PP2\Lab6\y.txt",os.X_OK))