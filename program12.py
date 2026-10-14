l1=list(map(int,input("enter first list: ").split()))
l2=list(map(int,input("enter second  list: ").split()))
print("same length : ",len(l1)==len(l2))
print("same sum : ",sum(l1)==sum(l2))
if set(l1)&set(l2):
	print("commom value exist!")
else:
	print("no common values!")
