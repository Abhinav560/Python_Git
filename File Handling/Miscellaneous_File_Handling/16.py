with open("file2.txt","r") as f:
    for line in reversed(f.readlines()):
        print(line.strip())