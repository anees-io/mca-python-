import Armstrong
lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
print("Armstrong number between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if Armstrong is armstrong(num):
        print(num,end=" ")

