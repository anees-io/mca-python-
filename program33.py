n=int(input("enter a number:"))
temp=n
total=0
power=len(str(n))

while temp>0:
    digit=temp%10
    total=total+digit**power
    temp=temp//10
if total==n:
    print("Armstrong number")
else:
    print("not Armstrong number")

