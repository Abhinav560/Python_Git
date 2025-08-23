num=int(input("enter a number:"))
if num<2:
    print("not a prime number.")
for i in range(2,num**0.5+1):
    if num%i==0:
        print("not a prime number")
    else:
        print("prime number")