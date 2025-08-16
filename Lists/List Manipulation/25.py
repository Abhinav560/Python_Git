mylist=[42,43,44,45,46,47,48]
chunk_size=3
chunks=[mylist[i:i + chunk_size] for i in range(0,len(mylist),chunk_size)]
print(chunks)