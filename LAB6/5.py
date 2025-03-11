a = list(map(str,input().split()))
f = open("C:/Users/TriumF/Documents/LAB6/dir_and_files/text.txt", "a")
for i in a:
    f.write(i+' ')
f.close()

f = open("C:/Users/TriumF/Documents/LAB6/dir_and_files/text.txt", "r")
print(f.read())