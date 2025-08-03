mylist=[1,2,3,4,5]
even_index_operations=[item*2 if i%2==0 else item for i,item in enumerate(mylist)]
print(even_index_operations)