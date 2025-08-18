with open("file2.txt","r") as f:
    data=f.read().replace("line","sentence")
with open("file2.txt","w") as f:
    f.write(data)