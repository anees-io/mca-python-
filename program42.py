def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter number of terms:"))
sum=0
for i in range (1,n+1):
    sum=sum+(i**i)/factorial(i)
print("sum of the series:",sum)
