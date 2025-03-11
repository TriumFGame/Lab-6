import os
path = r"D:\vs code\vscode\Code.exe"
print("exists or not:", os.path.exists(path))
print("\nFile name:", os.path.basename(path))
print("\nDir name:", os.path.dirname(path))