n=int(input())

for i in range(1,n):
    left=(" "*(n-i))
    num=""
    for k in range(1,i+1):
        num=num+"*"+" "
    print(left+num)
for row in range(1,n+1):
    
    left=(" "*(n-i))
    if i>1 and i<n:
        s=" "*(i-2)
        nk="* "+s+"* "+" "
        print(left+nk)
    else:
        s="* "*i 
        print(left+s)