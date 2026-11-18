import math
start=int(input("enter starting number:"))
end=int(input("enter ending number:"))

for n in range(max(start,1000),min(end,9999)+1):
    root=math.isqrt(n)
    
    if root*root==n:
        if all(int(digit)%2==0 for digit in str(n)):
            print(n)






























