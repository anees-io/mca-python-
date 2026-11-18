d1 = {}
d2 = {}
n1 =int (input("enter the number of items in first dictionary:"))
for i in range(n1):
    key = input("enter the key: ")
    value = int(input("enter value: "))
    d1[key] = value
n2 =int (input("enter the number of items in second dictionary:"))
for i in range(n2):
    key = input("enter the key: ")
    value = int(input("enter value: "))
    d2[key] = value
d1.update(d2)    
print("merged dictionary:",d1)
