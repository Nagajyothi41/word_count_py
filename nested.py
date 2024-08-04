def y(n):
    l=[]
    for i in n:
        p=int(i)
        l.append(p)
    return l 
m=int(input())
k=[]
for i in range(m):
    n=input().split()
    n=y(n)
    k.append(n)
print(k)    