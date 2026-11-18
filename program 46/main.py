import armstrong

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Armstrong numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    # Use a dot (.) to call the function from the module
    if armstrong.is_armstrong(num):
        print(num, end=" ")

