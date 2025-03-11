import os
print('Exist:', os.access("D:\vs code\vscode\Code.exe", os.F_OK))
print('Readable:', os.access("D:\vs code\vscode\Code.exe", os.R_OK))
print('Writable:', os.access("D:\vs code\vscode\Code.exe", os.W_OK))
print('Executable:', os.access("D:\vs code\vscode\Code.exe", os.X_OK))