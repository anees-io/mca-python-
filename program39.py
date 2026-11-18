def add(*args):
    """This function add variable number of integers."""
    total=0
    for i in args:
        total=total+i
    return total
print("sum=",add(10,20,30,40))
print("Documentation :",add.__doc__)
