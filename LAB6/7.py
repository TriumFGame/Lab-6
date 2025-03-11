with open("C:/Users/TriumF/Documents/LAB6/dir_and_files/text.txt",'r') as first, open("C:/Users/TriumF/Documents/LAB6/dir_and_files/text2.txt",'a') as second:
    for line in first:
        second.write(line)