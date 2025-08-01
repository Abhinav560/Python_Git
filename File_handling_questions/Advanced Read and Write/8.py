with open("file1.txt","r") as src, open("copy.txt","w") as dest:
    dest.write(src.read())