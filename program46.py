
    def is_armstrong(number):
    temp = num
    digits = len(str(number))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == number


# Example usage:
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

