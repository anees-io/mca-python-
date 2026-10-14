d = {}
n=int(input("enter the number of items:"))
for i in range(n):
    key = input("enter the key: ")
    value = int(input("enter value: "))
    d[key] = value
print("Ascending:",dict(sorted(d.items())))
print("Descending:",dict(sorted(d.items(),reverse=True)))
