num=int(input("enter the num upto which we want to add prime numbers:"))
prime_sum=0
for num in range(2,51):
    for i in range(2, num):
        if num%1==0:
            break
        else:
            prime_sum+=num
print(f"sum of prime numbers upto num: {prime_sum}")
