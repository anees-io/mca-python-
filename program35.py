def simple_interest(p, t, senior):
    if senior == "yes":
        r = 12
    else:
        r = 10

    si = (p * t * r) / 100
    return si

p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
senior = input("Senior citizen? (yes/no): ")

print("Simple Interest =", simple_interest(p, t, senior))
