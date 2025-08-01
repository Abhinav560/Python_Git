list=["line1\n","line2\n","line3\n"]
with open("file2.txt","w") as f:
    f.writelines(list)