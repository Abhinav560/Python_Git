mylist=[1,2,3,4,5,6,7,8]
chunk_size=3
chunks=[mylist[i:i + chunk_size] for i in range(0,len(mylist),chunk_size)]
print(chunks)