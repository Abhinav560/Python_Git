with open("file1.txt","r") as f:
    content=f.read()
    print("the count of words is:", len(content.split()))