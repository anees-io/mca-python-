names=input("enter names:").split()
count=0
for name in names:
    count+=name.lower().count('a')
print("numbers of occurence of 'a':",count)
