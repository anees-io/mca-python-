
def is_armstrong(number):
    temp = number
    digits = len(str(number))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == number



