num=int(input("enter the num upto which we want to add prime numbers:"))
prime_sum=0
for s in range(2,num):
    for i in range(2, s):
        if num%1==0:
            break
        else:
            prime_sum+=num
print(f"sum of prime numbers upto num: {prime_sum}")